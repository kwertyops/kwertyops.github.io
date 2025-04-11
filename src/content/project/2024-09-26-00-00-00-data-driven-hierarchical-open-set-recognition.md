---
title: "Data-Driven Hierarchical Open Set Recognition"
description: "40th IEEE International Conference on Robotics and Automation (ICRA@40), p.1835-1836"
pubDate: 2024-09-26 00:00:00
sourceUrl: "https://arxiv.org/abs/2411.02635"
authors: "Andrew Hannum, Max Conway, Mario Lopez, André Harrison"
tags: []
---

This paper presents a novel data-driven hierarchical approach to open set recognition (OSR) for robust perception in robotics and computer vision, utilizing constrained agglomerative clustering to automatically build a hierarchy of known classes in embedding space without requiring manual relational information. The method, demonstrated on the Animals with Attributes 2 (AwA2) dataset, achieves competitive results with an AUC ROC score of 0.82 and utility score of 0.85, while introducing two classification approaches (score-based and traversal-based) and a new Concentration Centrality (CC) metric for measuring hierarchical classification consistency. Although not surpassing existing models in accuracy, the approach provides valuable additional information about unknown classes through automatically generated hierarchies, requires no supplementary information beyond typical supervised model requirements, and introduces the Class Concentration Centrality (CCC) metric for evaluating unknown class placement consistency, with future work aimed at improving accuracy, validating the CC metric, and expanding to Large-Scale Open-Set Classification Protocols for ImageNet.
