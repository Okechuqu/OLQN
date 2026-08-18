# Delivery plan

## Recommended project structure

```text
OLQN/
├── apps/
│   ├── core/       # global settings, navigation, shared services
│   ├── home/       # homepage composition
│   ├── parish/     # about, clergy, sacraments, schedules, ministries
│   ├── events/     # calendar, registration, tickets, Paystack state
│   ├── news/       # bulletins, announcements, subscriptions
│   └── giving/     # campaigns, donations and receipts
├── config/settings/{base,dev,prod}.py
├── templates/{includes,home,parish,events,news,giving}/
├── static_src/{css,js}/
├── static/         # compiled frontend output
├── docs/
├── manage.py
├── pyproject.toml
├── package.json
└── render.yaml
```

## Stages and realistic speed

Assumption: one senior engineer, prompt access to approved copy, photographs,
Paystack keys, email-domain DNS and stakeholder feedback. A production-quality
release is approximately 8–10 weeks; a stable content-ready MVP is 4 weeks.

1. Discovery and content map — 2–3 days
   - Confirm information architecture, roles, payment flows and acceptance tests.
   - Inventory photography, logo sources, bulletins and privacy/finance policies.
2. Foundation and design system — 4–5 days
   - Poetry/Django/Wagtail/PostgreSQL, environments, CI, Tailwind tokens.
   - Mobile navigation, header/footer, accessible reusable components.
3. CMS pages — 7–9 days
   - Home, About, Mass Times, Sacraments, Ministries, Bulletins, Contact and search.
   - Editorial workflows, image rules, previews and content migration tools.
4. Events and ticketing — 7–10 days
   - Calendar/filtering, capacity, free/paid registration, Paystack idempotency,
     QR tickets, receipts, refunds/cancellations and staff check-in.
5. Giving and communications — 4–6 days
   - Campaigns, one-time giving, webhook verification, donor receipts.
   - Resend/Brevo templates, newsletter consent, suppression and reminders.
6. Admin, reporting and integrations — 4–5 days
   - Role-limited dashboards, exports, finance reconciliation and audit history.
   - Cloudinary transformations, Sentry release/error tracking, Cloudflare rules.
7. QA, security and launch — 5–7 days
   - Device/browser/accessibility tests, payment test matrix, backup restore drill,
     load tests, editor training, DNS rollout and production monitoring.

Parallel design/content preparation can reduce elapsed time, but payment testing,
editor acceptance and DNS/email verification remain launch gates.

## Performance budget

- Mobile Lighthouse target: Performance ≥ 90, Accessibility ≥ 95.
- LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 at the 75th percentile.
- Initial HTML ≤ 80 KB compressed; critical CSS + JS ≤ 150 KB compressed.
- Hero uses an explicit responsive rendition and `fetchpriority=high`.
- Below-fold images use Wagtail renditions, WebP/AVIF and native lazy loading.
- No blocking third-party scripts; analytics and embeds load after consent/intent.
- Cache public pages at Cloudflare; never cache admin, checkout or callbacks.
- Query budgets are asserted in tests; list pages use `select_related`/pagination.

## Non-negotiable payment and production controls

- Never trust browser payment success; verify reference, currency and amount with
  Paystack server-to-server before marking a record paid.
- Webhook HMAC verification, idempotent transitions and unique references.
- PostgreSQL transactions/row locking around capacity and payment transitions.
- Least-privilege CMS groups, MFA at providers, encrypted secrets and audit logs.
- Daily PostgreSQL backups plus a tested restore procedure.
- CSP, secure cookies, HSTS, rate limiting and Cloudflare bot/WAF rules.
- Sentry must redact personal/payment data; no card data is stored by OLQN.
