# Live readiness

- **Project:** Repo Steward Agent
- **Track:** Markee
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:14+00:00`

## Trust boundaries

- **Markee** — `rest_json` — Publish GitHub-adjacent build stories and repo messages.
- **OpenServ** — `rest_json` — Dispatch jobs and expose swarm service endpoints.
- **Filecoin** — `file_upload` — Persist proofs, logs, and evidence bundles offchain.
- **ENS** — `contract_call` — Publish human-readable coordination and identity receipts.
- **Bankr Gateway** — `rest_json` — Route inference through cost-aware model selection.
- **Octant** — `rest_json` — Publish scored public-goods signals and DPI artifacts.
- **Ampersend** — `rest_json` — Bundle payment and transport metadata for downstream agents.

## Offline-ready partner paths

- **Filecoin** — prepared_filecoin_bundle
- **ENS** — prepared_contract_call

## Live-only partner blockers

- **Markee**: MARKEE_API_KEY, MARKEE_MESSAGE_URL — https://markee.xyz/
- **OpenServ**: OPENSERV_API_KEY, OPENSERV_AGENT_URL — https://docs.openserv.ai/
- **Bankr Gateway**: BANKR_API_KEY, BANKR_CHAT_COMPLETIONS_URL, BANKR_MODEL — https://bankr.bot/
- **Octant**: OCTANT_SIGNAL_URL — https://octant.app/
- **Ampersend**: AMPERSEND_API_KEY, AMPERSEND_PAYMENT_URL — https://docs.ampersend.ai/

## Highest-sensitivity actions

- `bankr_gateway_compute_route` — Bankr Gateway — Use Bankr Gateway for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for RepoStewardCampaign.
- Run python3 scripts/run_agent.py to produce a dry run for repo_steward.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
