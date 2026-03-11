In this algorithm, we use hot-one to assign a value to a nucleotide. Then after performing Convolution on entire sequences, 
we can remove the in-between values.

We find the big values in this convolution and use it to find large clusters of same sub-sequence.
To improve the efficiency, we also find big jumps in these values and find the clusters of overlapping sub-sequences.

From my analysis, we can get satisfactory results for low values like 150 nucleotides each.
And not to mention Convolution have time complexity of O(nLog(n)).
Most of the algorithms like Needleman-Wunsch Algorithm which are used in advanced softwares like [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi) have complexity of O(n^2).

Genomic analysis is not my speciality so if you feel like any changes are needed, please feel free to contribute.
