import os, json
from reportlab.pdfgen import canvas
from azure.storage.blob import BlobServiceClient
from azure.identity import ManagedIdentityCredential

order_id    = os.environ["ORDER_ID"]
order       = json.loads(os.environ["ORDER_JSON"])
account_url = os.environ["STORAGE_ACCOUNT_URL"]
client_id   = os.environ.get("AZURE_CLIENT_ID")

# Generate PDF
pdf_path = f"/tmp/{order_id}.pdf"
c = canvas.Canvas(pdf_path)
c.drawString(100, 800, f"Order Report: {order_id}")
c.drawString(100, 780, f"Items: {len(order['items'])}")
y = 750
for item in order["items"]:
    c.drawString(100, y, f"  {item['sku']}  x{item['qty']}")
    y -= 20
c.save()

# Upload to blob using managed identity
svc  = BlobServiceClient(account_url=account_url, credential=ManagedIdentityCredential(client_id=client_id))
blob = svc.get_blob_client(container="reports", blob=f"{order_id}.pdf")
with open(pdf_path, "rb") as f:
    blob.upload_blob(f, overwrite=True)

print(f"Uploaded {order_id}.pdf to reports container")
