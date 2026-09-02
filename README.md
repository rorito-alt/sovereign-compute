# SovereignCompute

**A movement for citizen-owned, privacy-first, sustainable computing power.**

> The future of AI and scientific computing should not be controlled by a handful of corporations in distant data centers.  
> It should live in the hands of people — on devices we own, powered by energy we choose, serving causes we believe in.

SovereignCompute is both a **toolkit** and a **call to action**.

We are building the foundations of a global, decentralized compute network where ordinary people can contribute idle CPU/GPU cycles for:
- Climate modeling & environmental research
- Open scientific discovery
- Privacy-preserving AI inference
- Educational and public-good workloads

All while keeping data local, energy usage transparent, and ownership distributed.

## Why This Matters (The Movement)

Current AI and cloud computing is:
- Extremely energy-intensive
- Centralized in a few hyperscale data centers
- Privacy-invasive by design
- Locked behind expensive APIs and corporate gatekeepers

**SovereignCompute** proposes a different path:

1. **Local First** — Prefer running models and workloads on user-owned devices.
2. **Energy Aware** — Prefer clean energy and report carbon impact.
3. **Community Owned** — Shared governance, open protocols, no single point of control.
4. **Public Good Bias** — Prioritize workloads that benefit science, education, and the planet.

This is not just software. It is the seed of a new computing paradigm — one that treats compute as a commons rather than a commodity controlled by the few.

## Current Status (v0.1)

This repository currently contains:

- The **Manifesto** (see below)
- A minimal Python CLI prototype for local workload contribution simulation
- Contribution guidelines and roadmap
- MIT License

We are at the very beginning. Everything is open for contribution, critique, and evolution.

## The SovereignCompute Manifesto

**1. Compute is a Commons**  
Access to computing power should not be gated by wealth or corporate membership. Idle capacity on personal devices can and should serve the public good.

**2. Privacy is Non-Negotiable**  
No personal data leaves the device without explicit, informed consent. Workloads must be designed for local execution or strong cryptographic privacy.

**3. Energy Transparency**  
Every contribution reports estimated energy use and carbon intensity. Contributors can choose to prioritize clean-energy windows.

**4. Open Protocols Over Platforms**  
We build open standards so that many implementations can interoperate. No single company or foundation owns the network.

**5. Human Agency First**  
Technology serves people. Contributors decide what kinds of workloads they support. No forced participation.

**6. Sustainable by Design**  
Efficiency and longevity of hardware matter. We discourage wasteful computation and encourage repair, reuse, and right-to-repair principles.

## Quick Start (Prototype)

```bash
# Clone the repository
git clone https://github.com/rorito-alt/sovereign-compute.git
cd sovereign-compute

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install (currently pure Python, no heavy deps)
pip install -e .

# Run the prototype CLI
sovereign-compute --help
sovereign-compute contribute --duration 60 --workload climate
```

## Roadmap

### Phase 1 — Foundations (Now)
- [x] Manifesto & vision
- [x] Basic CLI prototype
- [ ] Formal open protocol specification (JSON/gRPC)
- [ ] Local workload runner (safe sandboxed execution)
- [ ] Carbon intensity awareness (using public electricity maps APIs)

### Phase 2 — Network
- [ ] Peer discovery & lightweight coordination layer
- [ ] Workload marketplace / matching (public-good priority)
- [ ] Reputation and contribution verification (without KYC)

### Phase 3 — Movement
- [ ] Educational materials & workshops
- [ ] Partnerships with research institutions and NGOs
- [ ] Hardware recommendations for efficient contribution nodes
- [ ] Governance model (DAO-like or federation)

## How to Contribute

We welcome:
- Protocol design discussions (open issues)
- Code for the local runner and CLI
- Documentation and translations of the manifesto
- Research on energy-efficient inference and scientific workloads
- Community organizing ideas

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

MIT License — free to use, modify, and distribute. See [LICENSE](LICENSE).

---

**Join the movement.**  
Star the repo. Open an issue. Fork it. Run it on your machine.  
The next era of computing will be built by many hands — starting with yours.

*Compute for the people. By the people. On the people's machines.*
