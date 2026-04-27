import os, json
from reportlab.pdfgen import canvas
from azure.storage.blob import BlobServiceClient

order_id   = os.environ["ORDER_ID"]
order      = json.loads(os.environ["ORDER_JSON"])
conn       = os.environ["STORAGE_CONN"]

# 1. Generate PDF locally
pdf_path = f"/tmp/{order_id}.pdf"
c = canvas.Canvas(pdf_path)
c.drawString(100, 800, f"Order Report: {order_id}")
c.drawString(100, 780, f"Items: {len(order['items'])}")
y = 750
for i, item in enumerate(order["items"]):
    c.drawString(100, y, f"  {item['sku']}  x{item['qty']}")
    y -= 20
c.save()

# 2. Upload to blob
svc = BlobServiceClient.from_connection_string(conn)
blob = svc.get_blob_client(container="reports", blob=f"{order_id}.pdf")
with open(pdf_path, "rb") as f:
    blob.upload_blob(f, overwrite=True)

print(f"Uploaded {order_id}.pdf to reports container")
