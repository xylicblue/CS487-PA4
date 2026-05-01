<div align="center">

# PA4 Submission: TaskFlow Pipeline

<img alt="GitHub only" src="https://img.shields.io/badge/Submit-GitHub%20URL%20Only-10b981?style=for-the-badge">
<img alt="Total points" src="https://img.shields.io/badge/Total-100%20points-7c3aed?style=for-the-badge">

</div>

<div style="background:#f5f3ff;color:#111827;border-left:6px solid #6330bc;padding:14px 18px;border-radius:10px;margin:18px 0;">
Copy this file to <code style="color:#111827;background:#ddd6fe;padding:2px 4px;border-radius:4px;">SUBMISSION.md</code>. Put every screenshot in <code style="color:#111827;background:#ddd6fe;padding:2px 4px;border-radius:4px;">docs/</code>, embed it under the correct task, and write a short description below each image explaining what it proves. The grader should not need any file outside this repository.
</div>

## Student Information

| Field | Value |
|---|---|
| Name | Mahad bin Aamir |
| Roll Number | 26100249 |
| GitHub Repository URL | https://github.com/xylicblue/CS487-PA4 |
| Resource Group | `rg-sp26-26100249` |
| Assigned Region | uk-west |

## Evidence Rules

- Use relative image paths, for example: `![AKS nodes](docs/aks-nodes.png)`.
- Every image must have a 1-3 sentence description below it.
- Azure Portal screenshots must show the resource name and enough page context to identify the service.
- CLI screenshots must show the command and output.
- Mask secrets such as function keys, ACR passwords, and storage connection strings.


## Task 1: App Service Web App (15 points)

### Evidence 1.1: Forked Repository

![description](forked_repo.png)

### Evidence 1.2: App Service Overview

![description](images/web_app_running.png)

Description: Web App pa4-26100249 running on B1 Linux App Service Plan in UK West, serving the TaskFlow frontend at https://pa4-26100249.azurewebsites.net

### Evidence 1.3: Deployment Center / GitHub Actions

![description](images/deployment_1.png)
![description](images/deployment_2.png)

### Application settings configured
![description](images/app_settings_configured.png)

Deployment Center connected to GitHub fork via GitHub Actions, automatically deploying on push to main.

### Evidence 1.4: Live Web UI

![description](images/web_app_running_azure.png)

TaskFlow order submission UI is live and accessible publicly.

---

## Task 2: Azure Container Registry (15 points)

### Evidence 2.1: ACR Overview

![description](images/acr_privisioned.png)

ACR pa426100249 (Basic SKU) in resource group rg-sp26-26100249, UK West.

### Evidence 2.2: Docker Builds

### Local Container Running:
![description](images/local_container_running.png)

# Building images locally:
![description](images/report-ss.png)
![description](images/validate-ss.png)
![description](images/funcapp-ss.png)

Three images built locally on docker : validate-api:v1, report-job:v1, func-app:v1.

### Local validator Test:
![description](images/local_curl_request.png)
Response:
![description](images/local_curl_req_resp.png)

### Pushing images to acr:
![description](images/push_acr_1.png)
![description](images/push_acr_2.png)

Images pushed to ACR with latest tag.

### Evidence 2.3: ACR Repositories

### Terminal:
![description](images/acr_verify_terminal.png)
### Azure GUI:
![description](images/acr_repo_azure_web.png)

Three images pushed: validate-api:v1, report-job:v1, func-app:v1

---

## Task 3: Durable Function Implementation (12 points)

### Evidence 3.1: Completed Function Code

`[function_app.py](function-app/function_app.py)`

The orchestrator chains validate_activity (calls AKS validator) → conditional reject or report_activity (spawns ACI to generate PDF).

### Evidence 3.2: Local Function Handler Listing

![description](images/azurite_ss.png)

---

## Task 4: Function App Container Deployment (8 points)

### Evidence 4.1: Function App Container Configuration

TODO: Embed screenshot showing the Function App uses your `func-app:v1` image from ACR.

Description: TODO: State the Function App name and image URI.

### Evidence 4.2: Orchestration Smoke Test

TODO: Embed screenshot of the `curl` output that starts an orchestration and returns status URLs.

Description: TODO: Explain what the returned `id` and `statusQueryGetUri` prove.

### Evidence 4.3: Expected Failed Status Before Downstream Wiring

TODO: Embed screenshot of the status query JSON showing the expected failure before `VALIDATE_URL` is configured.

Description: TODO: Explain why this failure is expected at this stage.

---

## Task 5: AKS Validator (15 points)

### Evidence 5.1: AKS Cluster

TODO: Embed screenshot of AKS overview showing `aks-<rollnum>` succeeded.

Description: TODO: State node count, node size, region, and resource group.

### Evidence 5.2: Kubernetes Nodes and Pods

TODO: Embed screenshot of `kubectl get nodes` and `kubectl get pods`.

Description: TODO: Explain that the validator pod is scheduled and running.

### Evidence 5.3: Kubernetes Service

TODO: Embed screenshot of `kubectl get service validate-service`.

Description: TODO: Identify the external IP and port exposed by the LoadBalancer.

### Evidence 5.4: Validator API Tests

TODO: Embed screenshot of `curl /health`, a valid `curl /validate`, and an invalid `curl /validate`.

Description: TODO: Explain the accepted path and the `qty > 100` rejection rule.

### Evidence 5.5: Function App `VALIDATE_URL`

TODO: Embed screenshot showing the Function App application setting `VALIDATE_URL`.

Description: TODO: Explain how the Durable Function reaches the AKS validator.

### Evidence 5.6: AKS Idle Behavior

TODO: Embed AKS metrics screenshot and/or `kubectl` output after the service is idle.

Description: TODO: Explain that the AKS node remains running even when there are no orders.

---

## Task 6: ACI Report Job (15 points)

### Evidence 6.1: Blob Container

TODO: Embed screenshot of the `reports` blob container.

Description: TODO: Explain where generated PDFs are stored.

### Evidence 6.2: Manual ACI Run

TODO: Embed screenshot of `az container show` for `ci-report-test`.

Description: TODO: State the final container state and why the job exits.

### Evidence 6.3: ACI Logs

TODO: Embed screenshot of `az container logs`.

Description: TODO: Explain what the report job printed after generating and uploading the PDF.

### Evidence 6.4: Generated PDF

TODO: Embed screenshot showing `TEST-001.pdf` in Blob Storage or opened from Blob Storage.

Description: TODO: Explain how this proves the ACI wrote to storage.

### Evidence 6.5: Function App Managed Identity and IAM

TODO: Embed screenshots of system-assigned identity enabled and Contributor role assignment on your resource group.

Description: TODO: Explain why the Function App needs this permission to create ACIs.

### Evidence 6.6: Report App Settings

TODO: Embed screenshot of `REPORT_*`, `ACR_*`, `STORAGE_CONN`, and `SUBSCRIPTION_ID` settings.

Description: TODO: Explain what each group of settings is used for. Mask secrets.

---

## Task 7: End-to-End Pipeline (15 points)

### Evidence 7.1: Web App Wiring

TODO: Embed screenshot showing `FUNCTION_START_URL` and `FUNCTION_STATUS_URL` configured on the Web App.

Description: TODO: Explain how the frontend starts and polls the Durable orchestration.

### Evidence 7.2: Happy Path UI

TODO: Embed screenshots of the form before submit, Running status, and Completed status with report URL.

Description: TODO: Explain the valid order payload and final result.

### Evidence 7.3: Backend Participation

TODO: Embed screenshots showing Function App invocation, AKS validator evidence, ACI evidence, and Blob PDF evidence.

Description: TODO: Trace the same order ID across services.

### Evidence 7.4: Reject Path UI

TODO: Embed screenshot of an order with `qty > 100` being rejected.

Description: TODO: Explain why no report ACI should be created for this order.

---

## Task 8: Write-up and Architecture Diagram (5 points)

### Evidence 8.1: Architecture Diagram

TODO: Embed your architecture diagram from `docs/`.

Description: TODO: Confirm that it shows GitHub, App Service, Durable Function, AKS, ACI, Blob Storage, ACR, and IAM.

### Question 8.2: Service Selection

TODO: In 3-4 sentences each, explain why TaskFlow uses App Service, Durable Functions, AKS, and ACI for their specific roles.

### Question 8.3: ACI vs AKS

TODO: Compare idle behavior, cost behavior, and operational model for AKS and ACI using your screenshots.

### Question 8.4: Durable Functions vs Plain HTTP

TODO: Explain at least two problems that Durable Functions solves for this sequential workflow.

### Question 8.5: Cost Review

TODO: Embed Cost Management screenshot scoped to your resource group.

Description: TODO: Identify the most expensive resource and explain why.

### Question 8.6: Challenges Faced

TODO: Describe at least two real issues you hit and how you debugged them.

---
