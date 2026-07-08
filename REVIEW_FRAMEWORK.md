# REVIEW_FRAMEWORK.md - Computational Science Review Checklist

Use this file to turn a paper into a research-group discussion, not a generic summary.

## General Computational Paper Review Logic

Ask these questions first:

- What is the unresolved problem?
- What is the old model, descriptor, or assumption?
- What changes in this paper?
- What computation supports the claim?
- What validates it?
- What assumptions could change the conclusion?
- What would we calculate next?

## DFT Review Focus

### Model System

- What atomic model is used?
- Is it a slab, bulk, molecule, defect, interface, or cluster?
- Are active sites, configurations, and coverages justified?
- Are finite-size effects important?

### Supercell / Slab / Interface

- Is the supercell large enough?
- Is the slab thick enough?
- Are vacuum, dipole correction, and boundary conditions appropriate?
- Are multiple terminations, facets, or defect configurations considered?

### Functional And Corrections

- Which exchange-correlation functional is used?
- Is dispersion included?
- Is Hubbard U used?
- Is spin polarization important?
- Could the conclusion depend on the functional?

### Solvation / Field / Potential

- Is solvation implicit, explicit, or absent?
- Is electric field or electrode potential treated?
- Are pH, ion, and electrolyte effects included?
- Are constant-charge and constant-potential assumptions separated?

### Free Energy

- Are zero-point energy and entropy corrections included?
- Are temperature effects included?
- Are vibrational, configurational, or solvent entropy terms important?
- Are thermodynamics and kinetics separated?

### NEB / Barriers

- Are transition states or migration barriers calculated?
- Are alternative pathways considered?
- Are barriers compared with experiment or known trends?

### Descriptors

- What descriptor is proposed?
- Is it mechanistic or just correlative?
- Does the descriptor survive a change in environment, coverage, or composition?

### Validation

- Is the result compared with experiment?
- Is it compared with previous DFT or higher-level theory?
- Are trends more important than absolute values?

## MLIP Review Focus

### Model Architecture

- What MLIP architecture is used?
- Is it equivariant, message-passing, kernel-based, moment-tensor, or another form?
- What quantities are predicted: energy, forces, stress, charge, or magnetic moments?

### Training Data

- What is the DFT reference level?
- How was the dataset generated?
- Does it cover phases, defects, surfaces, temperatures, pressures, and compositions?
- Is active learning used?
- Are high-energy, transition-state, or rare-event configurations included?

### Train / Test Split

- Is the test set independent?
- Is there an out-of-distribution test?
- Is the split random, structure-wise, composition-wise, or trajectory-wise?

### Error Metrics

- Energy RMSE
- Force RMSE
- Stress RMSE
- Relative energy ranking
- Barrier accuracy
- Phonon accuracy
- Structural stability

### MD Stability

- Does the MLIP remain stable in long MD?
- Does it conserve energy when appropriate?
- Does it reproduce structural, thermodynamic, or transport observables?

### Out-of-distribution Risk

- Are uncertainty estimates used?
- Are failure cases shown?
- Are long-range electrostatics, charge transfer, magnetism, or reactions important?
- Is extrapolation controlled?

### Physical Validation

- Does the MLIP reproduce DFT trends?
- Does it reproduce experimental observables?
- Does it enable new science beyond acceleration?

## AIMD / MD Review Focus

- What ensemble is used?
- Is the simulation time long enough?
- Is the system size large enough?
- Is sampling adequate?
- Are initial conditions biased?
- Are rare events accessible?
- Are finite-temperature effects essential to the claim?

## Discussion Prompts

Use 2-3 of these at the end:

- Which assumption most strongly controls the conclusion?
- What calculation would falsify the paper's mechanism?
- Is the model physically realistic enough for the claimed system?
- Does the validation test the central claim or only a side result?
- What would an MLIP, AIMD, or enhanced-sampling follow-up add?
- Which figure should we trust most, and which figure is weakest?
