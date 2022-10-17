# Midterm Progress
10/22/2022

## Project Description
Develop a desktop application to visualize Embrace2 datasets  
Provide a platform for data analysts to create unique views of Embrace2 data

## Team Structure
Derek Osborne - Project Manager - ZenHub / Designer / Reviewer  
Brad Adams - Software Developer - Backend  
Luke Rappa - Software Developer - UI / Layout  
Brenan Patrick - Software Developer - UI / Data Builder Tab  
Will Simpson -  Software Developer - UI / Data Visualization  

In terms of development, we help each other out in each item.  
Everyone is a developer on some item.  

## Features Planned for Project
- Develop a desktop application to visualize Embrace2 datasets
  - Provide UI to load individual datasets
    - Allow user to select which dimensions to load
    - Allow user to set if using UTC or Local System Time
  - Provide UI to visual loaded datasets
    - Use appropriate time series plots for each dimension selected
    - Provide UI to adjust the time window of the plots
    - Provide UI to zoom in / out of plots
    - Provide synchronization of plots based on time window
    - Provide UI to generate aggregate data for a data set

## Design of the Project
![Top-Down Design](../diagrams/top_down_design.JPG)  
- Key Ideas
  - One Top Level Window
    - Manage tabs and views created by user
  - One Data Builder Frame
    - UI for building dataset based on user parameters
  - Multiple Visualizer Frames
    - Contain X plots based on what user loads
    - Contains widgets to interact with data (specific to plots)
    - Contain Time Box to change date range of all plots synchronously
  - Composition
    - Lifetimes are bound to lifetime of the parent object
    - Allows easy closing of Visualizer Frames, let Garbage Collector clean up components

## Technology to Accomplish Project
- Application
  - Python 3.7+
  - Matplotlib
  - Tkinter
- Development
  - GitHub
  - ZenHub Extension
  - Diagrams.net

## Prototyping Results (WIP)

## Timeline / Adjustments