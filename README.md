# Methodology

## Population Selection and Data Processing
We will focus on populations represented in both databases, specifically:
- East Asian populations (CHB, JPT, CHS)
- European populations (CEU, TSI, FIN)
- African populations (YRI, LWK, ASW)
- Admixed populations (MXL, PUR)

## Analytical Approaches

### Population Structure Analysis
Rather than EIGENSTRAT (which we incorrectly specified), we will implement standard Principal Component Analysis using the smartpca program from the EIGENSOFT package. This analysis will:
1. Generate PCAs separately for both datasets
2. Identify corresponding principal components
3. Compare population clustering patterns

### Population Distance Metrics
We will implement multiple distance metrics to ensure robust comparison:
1. Traditional FST calculations using Hudson's estimator
2. Novel composite distance metric incorporating:
   - Euclidean distances in PCA space
   - Jensen-Shannon divergence of allele frequency spectra
   - LD pattern similarity scores

### Linkage Disequilibrium Analysis
Specific LD patterns to be investigated include:
1. Genome-wide LD decay curves calculated using:
   - r² values at different physical distances
   - Comparison of decay rates between populations
2. Haplotype block structure analysis:
   - Block identification using Gabriel's method
   - Comparison of block lengths and frequencies
3. Population-specific LD scores:
   - Calculation of LD score regression intercepts
   - Analysis of LD score correlation patterns

## Evaluation Framework
Results will be assessed through:
1. Quantitative Metrics:
   - Correlation coefficients between PCA coordinates
   - Statistical tests for significance of differences
   - Bootstrap confidence intervals for distance metrics
2. Qualitative Assessment:
   - Visual comparison of population clustering
   - Assessment of known historical relationships
   - Validation against documented admixture events

## Expected Outcomes
This analysis will provide:
1. Quantitative assessment of database consistency
2. Identification of systematic biases
3. Guidelines for database selection in population genetics studies
4. Recommendations for combined database usage
