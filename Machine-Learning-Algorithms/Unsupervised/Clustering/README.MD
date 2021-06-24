# Clustering in Machine Learning
> __It is basically a type of unsupervised learning method . An unsupervised learning method is a method in which we draw references from datasets consisting of input data without labelled responses. Generally, it is used as a process to find meaningful structure, explanatory underlying processes, generative features, and groupings inherent in a set of examples.
Clustering is the task of dividing the population or data points into a number of groups such that data points in the same groups are more similar to other data points in the same group and dissimilar to the data points in other groups. It is basically a collection of objects on the basis of similarity and dissimilarity between them.__

# Why Clustering ?
> __Clustering is very much important as it determines the intrinsic grouping among the unlabeled data present. 
> There are no criteria for a good clustering. It depends on the user, what is the criteria they may use which satisfy their need. For instance, we could be interested in finding representatives for homogeneous groups (data reduction), in finding “natural clusters” and describe their unknown properties (“natural” data types), 
> in finding useful and suitable groupings (“useful” data classes) or in finding unusual data objects (outlier detection). 
> This algorithm must make some assumptions which constitute the similarity of points and each assumption make different and equally valid clusters__

# Clustering Algorithms :
> 1. __K-means__
> 2. __Connectivity based methods :__ 1. Hierarchical clustering....
> 3. __Density Models :__ In this clustering model there will be a searching of data space for areas of varied density of data points in the data space . It isolates various density regions based on different densities present in the data space . 
For Ex- DBSCAN and OPTICS.  
> 4. __Subspace clustering :__ Subspace clustering is an unsupervised learning problem that aims at grouping data points into multiple clusters so that data point at single cluster lie approximately on a low-dimensional linear subspace. 
>  Subspace clustering algorithm localize the search for relevant dimension and allow to them to find cluster that exist in multiple overlapping subspaces. Subspace clustering was originally purpose to solved very specific computer vision problem having a union of subspace structure in the data but it gains increasing attention in the statistic and machine learning community. People use this tool in social network, movie recommendation, and biological dataset. Subspace clustering raise the concern of data privacy as many such application involve dealing with sensitive information. Data points are assumed to be incoherentas it only protects the differential privacy of any feature of a user rather than the entire profile user of the database. 
> * There are two branches of subspace clustering based on their search strategy. 

> 1. Top-down algorithms find an initial clustering in the full set of dimension and evaluate the subspace of each cluster.
> 2. Bottom-up approach finds dense region in low dimensional space then combine to form clusters.
