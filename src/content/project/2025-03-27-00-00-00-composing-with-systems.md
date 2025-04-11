---
title: "A Systematic Approach to Automated Generation of Guitar Chord Melody Études"
description: "Composing (with) Systems Conference 2025"
pubDate: 2025-03-27 00:00:00
sourceUrl: "https://chordmelody.io"
tags: []
---

Composing (with) Systems Conference 2025
Sheffield, UK

While computational approaches to musical composition have made significant strides in recent years, the generation of idiomatic instrumental music remains challenging, particularly for polyphonic instruments with complex physical constraints. We present a novel system for generating guitar chord melody arrangements that addresses the unique challenges of the instrument while maintaining musical coherence and pedagogical value.

Guitar chord melody style, where a single performer simultaneously executes melody and harmony, presents particular difficulties for computational generation due to the instrument's physical constraints and asymmetric layout. Our system implements a rule-based approach that resolves multiple simultaneous constraints: the selection of appropriate chord voicings, placement of melody notes, and determination of fretboard positions, all while ensuring physical playability.

Using Python and the music21 library for musical data processing, our system takes as input a melody and chord progression and produces complete arrangements through a systematic process. First, melodic notes are associated with underlying harmonies through a set of clear rules. Chord symbols are then realized through a sophisticated process that reduces complex harmonies to fundamental types, integrates melody notes, and generates appropriate drop voicings. Finally, fretboard positions are determined through an algorithm that balances playability constraints with musical preferences.

The system outputs professionally formatted scores and tablature using LilyPond, producing arrangements that are both musically satisfying and technically accessible. While designed with pedagogical applications in mind, the system also serves as a practical tool for exploring the space of possible chord melody arrangements.

Our presentation will include recorded demonstrations of the system, analysis of generated arrangements, and discussion of how our systematic approach could be extended to other situations or instrumental idioms. This work contributes to the broader field of algorithmic composition by demonstrating how domain-specific constraints can be effectively incorporated into the generation process while maintaining musical coherence.