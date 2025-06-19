# Gap-to-Greatness Roadmap

| Domain        | Directive                                                                                               |
| ------------- | ------------------------------------------------------------------------------------------------------- |
| Reliability   | Migrate to React-Query + Zustand offline cache with optimistic rollback.                                |
| Security      | OAuth PKCE for platform linking; AWS KMS key rotation; OWASP ZAP in CI.                                 |
| Scalability   | Split to Auth, Score, Ledger services behind API Gateway; Helm + HPA manifests.                         |
| Compliance    | Consent ledger APIs; PIPEDA export/delete jobs; Macie S3 DLP alarms.                                    |
| Observability | OpenTelemetry traces to Prometheus / Grafana; alert rules below.                                        |
| DX            | Storybook (native & web); auto-publish OpenAPI 3.1 to SwaggerHub.                                       |
| Analytics     | Emit Mixpanel events: platform_link_success, offer_view, loan_disbursed, repayment_success, error_type. |
| Performance   | Locust suite: 200 RPS, P95 <= 600 ms; cold-start lambda <= 600 ms.                                      |
