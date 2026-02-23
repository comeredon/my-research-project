"""Sample documents for the demo.

Contains excerpts and summaries from Microsoft Quantum research papers indexed
in the Azure AI Search instance backing this demo. The papers cover:
- QDK/Chemistry: quantum chemistry workflows on quantum hardware
- Interferometric single-shot parity measurement in InAs-Al hybrid devices
- Roadmap to fault-tolerant quantum computation using topological qubit arrays
- Optimizing the pairwise measurement-based surface code
"""

SAMPLE_DOCUMENTS = [
    {
        "title": "QDK/Chemistry: Introduction and Motivation",
        "source": "qkd-chemistry_a_modular_toolkit_for_quantum_chemistry_applications.pdf",
        "text": (
            "Quantum chemistry is among the most compelling application domains for "
            "quantum computers. The promise of efficiently simulating strongly correlated "
            "electronic systems, where classical methods face exponential scaling, has "
            "motivated extensive algorithmic development over the past two decades. "
            "Algorithms such as quantum phase estimation (QPE) and variational quantum "
            "eigensolver (VQE) provide frameworks for extracting ground state energies "
            "and properties, while advances in error correction bring fault-tolerant "
            "implementations within reach. QDK/Chemistry is an application library layer "
            "within the broader Microsoft Quantum Development Kit (QDK), which provides "
            "the underlying infrastructure for quantum algorithm development and execution. "
            "The QDK encompasses Q#, Qiskit, Cirq, and QASM programming languages for "
            "expressing quantum algorithms, compilers that translate high-level programs "
            "into optimized circuits, high-performance simulators for algorithm validation "
            "and debugging, and integrated development tooling within Visual Studio Code."
        ),
    },
    {
        "title": "QDK/Chemistry: Classical Electronic Structure Pipeline",
        "source": "qkd-chemistry_a_modular_toolkit_for_quantum_chemistry_applications.pdf",
        "text": (
            "Classical electronic structure methods provide the foundation for quantum "
            "chemistry workflows, generating the molecular orbitals, reference wavefunctions, "
            "and correlation treatments that serve as inputs for quantum algorithms. "
            "QDK/Chemistry manages molecular geometries through the Structure class, which "
            "represents atomic coordinates as immutable, self-contained objects. Self-Consistent "
            "Field (SCF) calculations, including Hartree-Fock, produce molecular orbitals as a "
            "reference starting point. Active space selection then identifies the subset of "
            "orbitals that capture the essential correlation physics while conforming to "
            "hardware qubit constraints. QDK/Chemistry supports fully automated active space "
            "selection using MP2 natural orbital occupancies or valence space methods, as well "
            "as manual expert specification. Multi-configuration methods such as CASCI and "
            "MCSCF generate high-quality initial states for quantum algorithms and provide "
            "classical baselines for comparison."
        ),
    },
    {
        "title": "QDK/Chemistry: Quantum Circuit Construction and QPE",
        "source": "qkd-chemistry_a_modular_toolkit_for_quantum_chemistry_applications.pdf",
        "text": (
            "Quantum circuit construction transforms classical electronic structure data into "
            "executable quantum programs, encompassing the encoding of molecular Hamiltonians "
            "onto qubits, preparation of initial quantum states, and extraction of observable "
            "estimates through measurement. Qubit Hamiltonian construction uses standard "
            "fermion-to-qubit mappings including the Jordan-Wigner, Bravyi-Kitaev, and parity "
            "transformations. State preparation maps classical wavefunction representations "
            "onto quantum circuits using sparse isometry encoding, which avoids exponential "
            "scaling for sparse wavefunctions. Quantum Phase Estimation (QPE) offers a "
            "fundamentally different paradigm from variational methods for extracting eigenvalues "
            "from quantum systems. In the context of active space methods, QPE can be viewed as "
            "a quantum CASCI solver that targets the same electronic structure problem within "
            "the defined active space, but executes on quantum hardware rather than classical "
            "processors, enabling chemical accuracy for systems where classical methods face "
            "fundamental scaling limitations."
        ),
    },
    {
        "title": "Interferometric Single-Shot Parity Measurement: Overview",
        "source": "interferometric_single-shot_parity_measurement.pdf",
        "text": (
            "The fusion of non-Abelian anyons or topological defects is a fundamental operation "
            "in measurement-only topological quantum computation. In topological superconductors, "
            "this operation amounts to a determination of the shared fermion parity of Majorana "
            "zero modes. This paper implements a single-shot interferometric measurement of "
            "fermion parity in indium arsenide-aluminum (InAs-Al) heterostructures with a "
            "gate-defined nanowire. The interferometer is formed by tunnel-coupling the "
            "proximitized nanowire to quantum dots. The nanowire causes a state-dependent shift "
            "of these quantum dots' quantum capacitance of up to 1 fF. Quantum capacitance "
            "measurements show flux h/2e-periodic bimodality with a signal-to-noise ratio of 1 "
            "in 3.7 microseconds at optimal flux values. Dwell time in the two associated states "
            "is longer than 1 ms at in-plane magnetic fields of approximately 2 T, consistent "
            "with measurement of fermion parity encoded in a pair of Majorana zero modes "
            "separated by approximately 3 micrometers. The large capacitance shift and long "
            "poisoning time enable a parity measurement error probability of 1%."
        ),
    },
    {
        "title": "Roadmap to Fault-Tolerant Quantum Computation: Tetron Architecture",
        "source": "roadmap_to_fault_tolerant_quantum_computation_using_topological_qubit_arrays.pdf",
        "text": (
            "This paper describes a concrete device roadmap towards a fault-tolerant quantum "
            "computing architecture based on noise-resilient, topologically protected "
            "Majorana-based qubits called tetrons. The roadmap encompasses four generations of "
            "devices: a single-qubit device that enables a measurement-based qubit benchmarking "
            "protocol; a two-qubit device that uses measurement-based braiding to perform "
            "single-qubit Clifford operations; an eight-qubit device that can demonstrate "
            "improvement of a two-qubit operation when performed on logical qubits rather than "
            "physical qubits; and a topological qubit array supporting lattice surgery "
            "demonstrations on two logical qubits. A tetron is formed through two parallel "
            "topological wires with a Majorana zero mode (MZM) at each end connected by a "
            "perpendicular trivial superconducting wire. Quantum dots adjacent to the MZMs, "
            "controlled by cutter gates, enable interferometric measurements via quantum "
            "capacitance shifts detectable using standard microwave techniques. Tetrons suppress "
            "idle and measurement errors exponentially in three dimensionless ratios: topological "
            "gap to temperature, wire length to topological coherence length, and measurement "
            "signal-to-noise ratio."
        ),
    },
    {
        "title": "Roadmap: Fault-Tolerant Quantum Error Correction and Lattice Surgery",
        "source": "roadmap_to_fault_tolerant_quantum_computation_using_topological_qubit_arrays.pdf",
        "text": (
            "Fault-tolerant quantum error correction is a crucial ingredient for any scalable "
            "quantum computing platform. For tetron qubits, a natural class of codes are the "
            "Hastings-Haah Floquet codes, which rely entirely on one- and two-body measurements "
            "to extract error syndromes, making them naturally well suited to the measurement-based "
            "tetron platform. The ladder code is a first demonstration, using few qubits but "
            "building on the same set of two-qubit measurements as scalable Floquet codes. "
            "Lattice surgery enables logical operations at scale: two logical qubit patches are "
            "stitched together into a larger patch to perform a two-logical-qubit measurement, "
            "then split back. For a utility-scale quantum computer of hundreds to thousands of "
            "logical qubits, tetrons have key advantages: with a single qubit area of roughly "
            "5 micrometers by 3 micrometers, millions of qubits fit on a single wafer; physical "
            "operations execute on microsecond timescales; and topological protection allows "
            "exponential reduction of error mechanisms through the topological gap over "
            "temperature ratio and wire length over coherence length ratio."
        ),
    },
    {
        "title": "Optimizing the Pairwise Measurement-Based Surface Code",
        "source": "optimizing_pairwise_measurement-based_surface_code.pdf",
        "text": (
            "The pairwise measurement-based surface code is a variant of the surface code "
            "optimized for architectures where two-body measurements are native operations, "
            "such as the tetron platform. The decoding pipeline uses the spacetime circuit "
            "formalism and constructs a decoding graph on which PyMatching v2 efficiently "
            "performs minimum weight perfect matching via the sparse blossom algorithm. "
            "A detector consists of a set of measurements for which the joint parity of "
            "outcomes is fixed in the absence of errors. Spacetime error chains correspond "
            "to collections of Pauli errors and readout errors on the circuit; an error chain "
            "is detectable if it triggers one or more detectors. Each vertex in the decoding "
            "graph is associated to a Z or X plaquette and a time coordinate. Vacancy mitigation "
            "techniques handle failed qubit components while preserving the code's error "
            "correction capability, requiring logical qubit patches with fault distance of at "
            "least 5. Sub-threshold operations demonstrate that logical error rates improve over "
            "physical error rates, a key milestone on the path to scalable fault-tolerant "
            "quantum computation."
        ),
    },
    {
        "title": "Majorana Zero Modes and Topological Protection",
        "source": "interferometric_single-shot_parity_measurement.pdf",
        "text": (
            "Majorana zero modes (MZMs) are exotic quasiparticles predicted to emerge at the "
            "boundaries of topological superconductors. Unlike conventional quasiparticles, "
            "MZMs are their own antiparticles and obey non-Abelian statistics, meaning the "
            "result of exchanging (braiding) two MZMs depends on the order of operations. "
            "This non-Abelian nature makes them attractive for topological quantum computation, "
            "where quantum information is encoded non-locally in the shared fermion parity of "
            "pairs of MZMs, providing inherent protection against local perturbations. In "
            "InAs-Al heterostructures, topological superconductivity is induced via the "
            "proximity effect: aluminum contacts a semiconductor nanowire, and under an "
            "applied magnetic field exceeding the topological phase transition, MZMs form at "
            "the wire ends. The fermion parity of two MZMs — either even or odd — encodes one "
            "qubit of quantum information. Reading this parity requires an interferometric "
            "measurement that couples the MZMs to quantum dots, converting the parity state "
            "into a measurable quantum capacitance signal."
        ),
    },
    {
        "title": "QDK/Chemistry: End-to-End Workflow Example",
        "source": "qkd-chemistry_a_modular_toolkit_for_quantum_chemistry_applications.pdf",
        "text": (
            "A complete QDK/Chemistry workflow demonstrates the modular design from molecular "
            "geometry specification through quantum phase estimation. The workflow begins by "
            "defining a Structure object with atomic coordinates — for example, a stretched H2 "
            "molecule. A PySCF SCF solver then computes the mean-field reference wavefunction. "
            "An active space selector using valence space parameters reduces the problem to "
            "a manageable set of orbitals and electrons. A CASCI solver generates a "
            "multi-configuration wavefunction as the initial state for the quantum algorithm. "
            "The Hamiltonian is encoded onto qubits using a Jordan-Wigner or Bravyi-Kitaev "
            "mapping. A state preparation circuit encodes the CASCI wavefunction. Finally, "
            "quantum phase estimation on a fault-tolerant quantum computer extracts the ground "
            "state energy to chemical accuracy. The factory pattern (algo.create) and common "
            "interface (run method) allow seamless substitution of classical or quantum backends "
            "at each stage, enabling both simulation-based and hardware-based execution."
        ),
    },
]

# Metadata about the research papers in this corpus
PAPER_METADATA = {
    "qkd-chemistry_a_modular_toolkit_for_quantum_chemistry_applications.pdf": {
        "title": "QDK/Chemistry: A Modular Toolkit for Quantum Chemistry Applications",
        "organization": "Microsoft Quantum",
        "topic": "Quantum Chemistry",
        "description": (
            "Describes the Microsoft Quantum Development Kit chemistry library, covering "
            "the full pipeline from molecular geometry specification to QPE-based energy "
            "estimation on fault-tolerant quantum hardware."
        ),
    },
    "interferometric_single-shot_parity_measurement.pdf": {
        "title": "Interferometric Single-Shot Parity Measurement in InAs-Al Hybrid Devices",
        "organization": "Microsoft Azure Quantum",
        "topic": "Topological Qubits / Majorana",
        "description": (
            "Demonstrates single-shot measurement of fermion parity in InAs-Al "
            "heterostructures, a foundational step toward topological quantum computation "
            "using Majorana zero modes."
        ),
    },
    "roadmap_to_fault_tolerant_quantum_computation_using_topological_qubit_arrays.pdf": {
        "title": "Roadmap to Fault-Tolerant Quantum Computation Using Topological Qubit Arrays",
        "organization": "Microsoft Quantum",
        "topic": "Fault-Tolerant Quantum Computing / Tetrons",
        "description": (
            "Presents a four-generation device roadmap from single tetron qubits to "
            "utility-scale fault-tolerant quantum computing, using Hastings-Haah Floquet "
            "codes and lattice surgery."
        ),
    },
    "optimizing_pairwise_measurement-based_surface_code.pdf": {
        "title": "Optimizing the Pairwise Measurement-Based Surface Code",
        "organization": "Microsoft Quantum",
        "topic": "Quantum Error Correction",
        "description": (
            "Details optimization of the surface code variant suited to pairwise "
            "measurement-based architectures, including decoding graph construction, "
            "PyMatching v2 decoding, and vacancy mitigation."
        ),
    },
}

# ---------------------------------------------------------------------------
# MCP Demo: Agent Reasoning Over Azure AI Search Results
# ---------------------------------------------------------------------------
# Each entry represents a real scenario from querying the Azure AI Search MCP
# server backing this demo. The 'mcp_raw_results' simulate what the MCP tool
# actually returns (id, location, content, @search.score). The 'answer_without_mcp'
# shows a generic training-data response; 'answer_with_mcp' shows what the agent
# produces after querying the index and reasoning over the retrieved chunks.
MCP_DEMO_RESULTS = [
    {
        "question": "How does quantum phase estimation extract molecular ground state energies?",
        "mcp_tool": "hybrid_search",
        "mcp_query": "quantum phase estimation molecular ground state energy chemistry",
        "mcp_raw_results": [
            {
                "id": "qkd-chemistry-chunk-042",
                "location": "qkd-chemistry_a_modular_toolkit_for_quantum_chemistry_applications.pdf",
                "@search.score": 0.9421,
                "content": (
                    "Quantum Phase Estimation (QPE) offers a fundamentally different paradigm "
                    "from variational methods for extracting eigenvalues from quantum systems. "
                    "In the context of active space methods, QPE can be viewed as a quantum CASCI "
                    "solver that targets the same electronic structure problem within the defined "
                    "active space, but executes on quantum hardware rather than classical processors, "
                    "enabling chemical accuracy for systems where classical methods face fundamental "
                    "scaling limitations."
                ),
            },
            {
                "id": "qkd-chemistry-chunk-017",
                "location": "qkd-chemistry_a_modular_toolkit_for_quantum_chemistry_applications.pdf",
                "@search.score": 0.8873,
                "content": (
                    "A complete QDK/Chemistry workflow begins by defining a Structure object "
                    "with atomic coordinates. A PySCF SCF solver computes the mean-field reference "
                    "wavefunction. An active space selector using valence space parameters reduces "
                    "the problem to a manageable set of orbitals and electrons. The Hamiltonian is "
                    "encoded onto qubits using a Jordan-Wigner mapping. State preparation encodes "
                    "the CASCI wavefunction. Finally, QPE on a fault-tolerant quantum computer "
                    "extracts the ground state energy to chemical accuracy."
                ),
            },
            {
                "id": "qkd-chemistry-chunk-031",
                "location": "qkd-chemistry_a_modular_toolkit_for_quantum_chemistry_applications.pdf",
                "@search.score": 0.8104,
                "content": (
                    "Quantum circuit construction transforms classical electronic structure data "
                    "into executable quantum programs. State preparation maps classical wavefunction "
                    "representations onto quantum circuits using sparse isometry encoding, which "
                    "avoids exponential scaling for sparse wavefunctions. Qubit Hamiltonian "
                    "construction uses the Jordan-Wigner, Bravyi-Kitaev, and parity transformations."
                ),
            },
        ],
        "answer_without_mcp": (
            "Quantum phase estimation (QPE) is a quantum algorithm that estimates the "
            "eigenvalues of a unitary operator. For molecular systems, QPE is applied to the "
            "time-evolution operator of the molecular Hamiltonian. The algorithm uses a "
            "register of ancilla qubits and controlled operations to extract the phase, which "
            "encodes the ground state energy. The result is more accurate than classical methods "
            "for strongly correlated systems."
        ),
        "agent_reasoning_steps": [
            "🔍 Queried Azure AI Search with: 'quantum phase estimation molecular ground state energy chemistry'",
            "📄 Retrieved 3 chunks (scores: 0.94, 0.89, 0.81) — all from QDK/Chemistry paper",
            "🧩 Chunk 1: QPE framed as a quantum CASCI solver operating within an active space",
            "🧩 Chunk 2: Full workflow — Structure → SCF → active space → Jordan-Wigner → QPE",
            "🧩 Chunk 3: Circuit construction details — sparse isometry encoding for state prep",
            "✍️  Synthesising: QPE is not standalone — it sits at the end of a classical/quantum pipeline",
        ],
        "answer_with_mcp": (
            "According to the **QDK/Chemistry paper** (indexed in Azure AI Search), QPE "
            "functions as a *quantum CASCI solver* — it does not operate on the full molecular "
            "Hamiltonian but on an **active space** selected from the SCF reference wavefunction. "
            "The pipeline is: (1) define molecular geometry via a `Structure` object, (2) run "
            "Hartree-Fock (SCF) with PySCF, (3) select an active space using MP2 natural orbital "
            "occupancies, (4) encode the Hamiltonian onto qubits via the **Jordan-Wigner mapping**, "
            "(5) prepare the initial state using sparse isometry encoding of the CASCI "
            "wavefunction, (6) run QPE on fault-tolerant hardware to extract the ground state "
            "energy to chemical accuracy. The key advantage over VQE is that QPE provides a "
            "provably accurate estimate without classical optimisation loops."
        ),
    },
    {
        "question": "What is a tetron qubit and how does it protect quantum information?",
        "mcp_tool": "hybrid_search",
        "mcp_query": "tetron qubit topological protection Majorana zero modes exponential suppression",
        "mcp_raw_results": [
            {
                "id": "roadmap-chunk-008",
                "location": "roadmap_to_fault_tolerant_quantum_computation_using_topological_qubit_arrays.pdf",
                "@search.score": 0.9611,
                "content": (
                    "A tetron is formed through two parallel topological wires with a Majorana "
                    "zero mode (MZM) at each end connected by a perpendicular trivial "
                    "superconducting wire. Quantum dots adjacent to the MZMs, controlled by cutter "
                    "gates, enable interferometric measurements via quantum capacitance shifts "
                    "detectable using standard microwave techniques. Tetrons suppress idle and "
                    "measurement errors exponentially in three dimensionless ratios: topological "
                    "gap to temperature, wire length to topological coherence length, and "
                    "measurement signal-to-noise ratio."
                ),
            },
            {
                "id": "roadmap-chunk-003",
                "location": "roadmap_to_fault_tolerant_quantum_computation_using_topological_qubit_arrays.pdf",
                "@search.score": 0.9102,
                "content": (
                    "The roadmap encompasses four generations of devices: a single-qubit device "
                    "enabling measurement-based qubit benchmarking; a two-qubit device using "
                    "measurement-based braiding for single-qubit Clifford operations; an eight-qubit "
                    "device demonstrating improvement of two-qubit operations on logical vs physical "
                    "qubits; and a topological qubit array supporting lattice surgery demonstrations "
                    "on two logical qubits."
                ),
            },
            {
                "id": "parity-chunk-011",
                "location": "interferometric_single-shot_parity_measurement.pdf",
                "@search.score": 0.8344,
                "content": (
                    "Majorana zero modes (MZMs) are their own antiparticles and obey non-Abelian "
                    "statistics. Quantum information is encoded non-locally in the shared fermion "
                    "parity of pairs of MZMs, providing inherent protection against local "
                    "perturbations. In InAs-Al heterostructures, topological superconductivity "
                    "is induced via the proximity effect under an applied magnetic field."
                ),
            },
        ],
        "answer_without_mcp": (
            "A tetron is a type of topological qubit based on Majorana zero modes. It uses "
            "two topological nanowires joined together. The quantum information is protected "
            "topologically, meaning local noise does not easily corrupt the qubit state. "
            "Tetrons are part of Microsoft's approach to building a fault-tolerant quantum computer."
        ),
        "agent_reasoning_steps": [
            "🔍 Queried Azure AI Search with: 'tetron qubit topological protection Majorana zero modes exponential suppression'",
            "📄 Retrieved 3 chunks from roadmap paper (0.96, 0.91) and parity paper (0.83)",
            "🧩 Chunk 1 (roadmap): Exact device geometry — two parallel topological wires + MZMs at ends",
            "🧩 Chunk 1 (roadmap): Error suppression formula — 3 dimensionless ratios (gap/T, length/ξ, SNR)",
            "🧩 Chunk 2 (roadmap): Four-generation device roadmap with concrete milestones",
            "🧩 Chunk 3 (parity paper): Physical basis — non-Abelian statistics, non-local encoding",
            "✍️  Cross-paper synthesis: geometry (roadmap) + physical protection mechanism (parity paper)",
        ],
        "answer_with_mcp": (
            "A **tetron** (from the **Roadmap paper**) is a Majorana-based qubit built from "
            "**two parallel topological nanowires**, each hosting a Majorana zero mode (MZM) "
            "at its ends, connected by a perpendicular superconducting wire. Cutter gates expose "
            "MZMs to adjacent quantum dots, enabling **interferometric qubit readout** via "
            "quantum capacitance shifts.\n\n"
            "Protection is **exponential**, not polynomial, in three dimensionless ratios:\n"
            "- **Topological gap / temperature** — larger gap → fewer thermal excitations\n"
            "- **Wire length / coherence length** — longer wire → better MZM separation\n"
            "- **Measurement SNR** — better readout → fewer measurement errors\n\n"
            "The physical basis (from the **Interferometric Parity paper**) is that information "
            "is encoded *non-locally* in the shared fermion parity of an MZM pair — a local "
            "perturbation must affect both MZMs simultaneously to corrupt the qubit, which is "
            "exponentially suppressed by the wire length."
        ),
    },
    {
        "question": "How is fermion parity measured, and what is the error probability?",
        "mcp_tool": "hybrid_search",
        "mcp_query": "fermion parity measurement InAs aluminum interferometric quantum capacitance signal noise",
        "mcp_raw_results": [
            {
                "id": "parity-chunk-001",
                "location": "interferometric_single-shot_parity_measurement.pdf",
                "@search.score": 0.9788,
                "content": (
                    "This paper implements a single-shot interferometric measurement of fermion "
                    "parity in indium arsenide-aluminum (InAs-Al) heterostructures with a "
                    "gate-defined nanowire. The interferometer is formed by tunnel-coupling the "
                    "proximitized nanowire to quantum dots. The nanowire causes a state-dependent "
                    "shift of the quantum dots' quantum capacitance of up to 1 fF."
                ),
            },
            {
                "id": "parity-chunk-007",
                "location": "interferometric_single-shot_parity_measurement.pdf",
                "@search.score": 0.9512,
                "content": (
                    "Quantum capacitance measurements show flux h/2e-periodic bimodality with a "
                    "signal-to-noise ratio of 1 in 3.7 microseconds at optimal flux values. Dwell "
                    "time in the two associated states is longer than 1 ms at in-plane magnetic "
                    "fields of approximately 2 T, consistent with measurement of fermion parity "
                    "encoded in a pair of Majorana zero modes separated by approximately 3 micrometers. "
                    "The large capacitance shift and long poisoning time enable a parity measurement "
                    "error probability of 1%."
                ),
            },
            {
                "id": "parity-chunk-014",
                "location": "interferometric_single-shot_parity_measurement.pdf",
                "@search.score": 0.8901,
                "content": (
                    "The fusion of non-Abelian anyons is a fundamental operation in measurement-only "
                    "topological quantum computation. In topological superconductors, this amounts to "
                    "a determination of the shared fermion parity of Majorana zero modes. Dwell time "
                    "longer than 1 ms confirms the quasiparticle poisoning rate is sufficiently low "
                    "for quantum error correction protocols."
                ),
            },
        ],
        "answer_without_mcp": (
            "Fermion parity in Majorana devices is measured interferometrically. The Majorana "
            "zero modes are coupled to a quantum dot or similar detector, and the parity state "
            "determines a measurable quantum property such as conductance or capacitance. "
            "The measurement needs to be fast compared to the decoherence time."
        ),
        "agent_reasoning_steps": [
            "🔍 Queried Azure AI Search with: 'fermion parity measurement InAs aluminum interferometric quantum capacitance signal noise'",
            "📄 Retrieved 3 chunks from interferometric parity paper (scores: 0.98, 0.95, 0.89)",
            "🧩 Chunk 1: Device geometry — InAs-Al nanowire tunnel-coupled to quantum dots; capacitance shift up to 1 fF",
            "🧩 Chunk 2: Quantitative results — SNR=1 in 3.7 µs, dwell time >1 ms at 2 T, MZM separation 3 µm, error prob 1%",
            "🧩 Chunk 3: Context — why dwell time >1 ms matters for QEC protocols",
            "✍️  All three chunks from same paper — high confidence answer with specific experimental numbers",
        ],
        "answer_with_mcp": (
            "From the **Interferometric Parity Measurement paper** (Azure AI Search):\n\n"
            "**Mechanism**: The proximitized InAs-Al nanowire is tunnel-coupled to quantum dots. "
            "The fermion parity of the MZM pair causes a **state-dependent quantum capacitance shift "
            "of up to 1 fF** in the quantum dots — this capacitance difference is the measurement signal.\n\n"
            "**Key experimental numbers**:\n"
            "- Magnetic field: ~**2 T** in-plane (required to enter the topological phase)\n"
            "- MZM separation: ~**3 micrometers** along the wire\n"
            "- Measurement SNR = 1 achieved in **3.7 microseconds**\n"
            "- State dwell time: **> 1 millisecond** (quasiparticle poisoning suppressed)\n"
            "- **Parity measurement error probability: 1%**\n\n"
            "The long dwell time (1 ms >> 3.7 µs measurement time) confirms the quasiparticle "
            "poisoning rate is low enough for quantum error correction — a prerequisite for the "
            "tetron roadmap."
        ),
    },
]
