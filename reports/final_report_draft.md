#Final Report Draft

##Freshman Plague
###An Epidemiological Story
Starring: Matthew Ruehle, Sean Carter, and Gabriel Butterick


2) An abstract that identifies the topics you investigate and the tools you use.
We investigated the spread of the Freshman plague through the student population using a Python implementation of BA graphs to represent the population, the edges of the graph to represent social relationships, and the effect of "infectious but unaware" time periods. In an attempt to make the model sufficiently, but not overbearingly, realistic, we customized the social relationships to reflect roommate pairs as well as varying degrees of closeness among friends. We used the "infectious but unaware" time to emulate the way people sequester themselves once they know they're sick to see how that would change the spread of disease.

3) An annotated bibliography of 3-5 papers that relate to your topic and/or tools. Explain what the papers are about, what experiments they report, and what their primary conclusions are.

##Annotated Bibliography
Lander Willem et. al. "Optimizing Agent Based Models for Infectious Diseases"

Downloaded from http://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-015-0612-2 (Links to an external site.) 9-27-16

The purpose of this paper is to examine optimization avenues available to agent based models of infectious disease transmission. The bulk of the paper revolves around describing the models, the optimizations for the models, and the resulting efficiency gains of the optimization. A more promising optimization they pursued was in clustering agents based on state and selectively performing calculations in order to avoid needless computation.


Cindy Hui, Mark Goldberg, Malik Magdon-Ismail, William A. Wallace: Simulating the Diffusion of Information: An Agent-based Modeling Approach

Link: http://www.cs.rpi.edu/~goldberg/publications/ads-journal.pdf 

This paper investigates the way that the preferences of agents can allow information about evacuation warnings to spread throughout a social network. It used variations of trust distribution, strategy for seeding the information, to explore the diffusion process.


Miksch, Urach, Einzinger, Zauner, "A Flexible Agent-Based Framework for Infectious Disease Modeling"

2014, University of the Philippines Cebu & Vienna Institute of Technology.  http://link.springer.com/chapter/10.1007%2F978-3-642-55032-4_4 (Links to an external site.)

An agent-based model provides a reasonable approximation of infectious diseases' spreads; epidemic behavior emerges naturally from a model with factors like an agent's susceptibility, health, and likelihood to spread the disease to other agents. The chief concern, then, is that these models require extensive "background" information: these parameters, for example, are difficult to measure, but the efficacy of the model in predicting real-world behavior rely on knowing them for a human population.


4) For each experiment you performed, present your question, methodology, results, and interpretation. Your draft final report should include at least one experiment that is substantially complete. If you have additional experiments in progress, you should draft those sections and include place-keepers for the results and interpretation.

##Experiments Performed

###1. Our first experiment was created to differentiate the spread of disease through a college campus from the spread of disease elsewhere. Our starting point was a Barabasi-Albert graph, which is already created to model a social network.

Question: How does adding very strong random roomate edges to a BA graph change the speed with which disease propogates through our network, and how does this change the maximum number of people that become infected?

Methodology: We generated a BA graph based on the model from chapter 4 in ThinkComplexity. We modified it so that each node is a students object, with an ability to spread disease, an ability to resist disease, and a state (healthy, infected, or immune). We decided that infectio should be spread by prolonged exposure - each timestep, a person can be given infection by nearby nodes that are infected, untill they pass a threshold that lables them as infected as well.

After this, we implemented another function that would set edges between pairs of nodes to a maximum social bond at random (to simulate random roomate assignment in freshman year), and compared the results obtained from otherwise random graphs.

Results:

Ovserved trends over 100 runs:

![Peak sick nodes](imgs/max_infected_cdf.png)
![Average sick nodes](imgs/average_infected_cdf.png)

Infection durring a single run:

![Single run, without roommates.](imgs/single_iter_NR.png)
![Single run, with roommates.](imgs/single_iter_R.png)

Interpretation: As one might expect, both the total and peak number of infected nodes is greater in the graph with roommates. This can be partly attributed to just the exposure of the roommate - but, moreso the "small world" effect of ties between random nodes in a BA graph - increasing the odds of an early infection reaching a "popular" node.


###Question: How is disease spread affected by the interplay between self-quarantining, and an asymptomatic-but-virulently-infectious stage?

Methodology: By looking into the dynamics behind the real-world disease measles - containing, among other things, several days of heightened infectiousness but minimal symptoms - and considering the self-quarantining which most people display while ill (staying home, avoiding additional social engagements, &c.), we wrote a version of the disease which would change its infectiousness over time.

Results:
'Measles' vs 'Non-measles' infection dynamic, one run:
![Single run, measles infectious step](imgs/measles_onerun_numsick_overtime.png)
![Single run, standard infectious step](imgs/notmeasles_onerun_numsick_overtime.png)

Quarantine strength, one run:
![No self-quarantine](imgs/no_sq.png)
![Partial self-quarantine](imgs/some_sq.png)
![Perfect self-quarantine](imgs/all_sq.png)

Quarantine strength, CDF of 100 runs:
_TODO. Will run and put here by the final report._

Interpretation: Increasing the virulence of the disease, as expected, also sharply increases both the peak and the mean number of infected nodes. We further observed that the strength of the self-imposed quarantine plays a significant role - as one would expect - in how quickly the disease manages to spread.
We speculate that part of the virulence of the "Freshman Plague" in particular can be attributed to the weakness of students' self-quarantines, especially in their first year. A strong or perfect quarantine, after all, leads to diseases which "die out" after just a few steps; unfortunately, a plethora of obligations (meeting new people, joining new activities, and coursework) keep even particularly sick students from achieving an effective self-imposed quarantine; this could explain some of why the plague also appears to manifest itself chiefly in the new class each year.





5) Reflect on your learning goals. You should already have paragraph for each team member that explains your learning goals for the second half of the semester and how this project is helping you achieve those goals. This is a good time to reflect on those goals and consider whether you are on target to reach them.

Gabe: Though the BA graph isn't your average cellular automata, you can definitely abstract cellular automata out to be a network graph of relationships. Considering that each node on the BA graphs we generated had a variety of states, and the relationships between nodes was unique, I would say you could call what we did a complex cellular automata, at least for a very loose definition of one. We definitely had the option to make the model much more time intensive, but through a variety of design and implementation decisions we managed to make the model give valuable information while not taking a ton of time and computational power to run, which I consider a success. We didn't do very much with evaluating the efficiency of the model, but that proved unnecessary anyway.

Matt: Looking back, I contend I met my learning goals fairly well--we implemented a network of agents, modeled behavior, and interpreted its results in an explanatory context. Insofar as efficiency is concerned, the model is not particularly optimized--but, doesn't appear to have any easily-resolved "sinks" either.

Sean: I think that I feel pretty good about our model, and my highest priorety was implimenting a high quality model without guidence. There wasn't as much in the way of a novel programming challenge with our project as I might have hoped, but it wasn't completely trivial either. My other goal was to create interesting visualization, and I think that our graphs are excellent.

