# Genetic Algorithm Hello World

Simple python script wrote by me after reading a book about genetic algorithms and neural networks a while ago.  
Code is poorly commented, so it is not advisable to dive into it.  

**What does this code do?**  
Basically, the code generates population of chromosomes.  
Chromosome consists of *gene* and *fitness value*.  
Gene is a list of numeric values.  
Program generates random chromosomes and tries to maximize fitness value using *Genetic Algorithm*.  
After it succeeded, we will get output like this:
```
Generation: 0, Average fitness: 27.4, Best: 36, Pop count: 115
Generation: 1, Average fitness: 28.719298245614034, Best: 36, Pop count: 114
Generation: 2, Average fitness: 30.52252252252252, Best: 37, Pop count: 111
Generation: 3, Average fitness: 32.5, Best: 40, Pop count: 110
Generation: 4, Average fitness: 34.76106194690266, Best: 40, Pop count: 113
Generation: 5, Average fitness: 36.414414414414416, Best: 44, Pop count: 111
Generation: 6, Average fitness: 37.71028037383178, Best: 45, Pop count: 107
Generation: 7, Average fitness: 39.28448275862069, Best: 47, Pop count: 116
Generation: 8, Average fitness: 41.20175438596491, Best: 47, Pop count: 114
Generation: 9, Average fitness: 42.554545454545455, Best: 47, Pop count: 110
Generation: 10, Average fitness: 43.62280701754386, Best: 49, Pop count: 114
Generation: 11, Average fitness: 44.78378378378378, Best: 49, Pop count: 111
Generation: 12, Average fitness: 45.86363636363637, Best: 49, Pop count: 110
Generation: 13, Average fitness: 46.65765765765766, Best: 49, Pop count: 111
Generation: 14, Average fitness: 47.11711711711712, Best: 50, Pop count: 111
Done!
Best fitness: 50
Worst fitness: 44
```

Feature checklist:  
- [x] 3 types of selection.  
- [x] 2 types of crossover.  
- [x] 2 types of fitness scaling. 
- [x] It works.  
- [ ] Multithreading.  
- [ ] Clear and understandable code.  
- [ ] Convenient library interface.  
