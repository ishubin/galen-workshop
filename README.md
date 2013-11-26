Galen Workshop
========

This project will soon be filled with different small test projects as part of Galen Framework workshops.
I am still not sure about the format and what exactly should fit in each workshop so the content of sections might change a bit.

Part 1. Introduction to Galen. Writing a simple test set for a responsive website. Basic set of Galen specs
--------
We will try to perform a basic testing of webpage skeleton
### Purpose
* Testing the basic skeleton of web page
* Optimization in page specs
* Basic test suite optimization

### Exercise
http://samples.galenframework.com/tutorial1/tutorial1.html

The workshop is finished. The contents are in workshop-01 folder


Part 2. Advanced testing
------
### Purpose
* Sections and reporting. Lets make a nicer feedback in Html reports
* Template specs. Implement tests for menu. Use the web page from tutorial1
* Testing form elements.

### Exercise 
Will follow up soon




The following are just drafts
----------

####Test Suite Parameterizations
* How to do multi-level paramerizations
* Merging tables

####Importing specs
Share common objects between different page specs (e.g. header, footer)

####Corrections
Website alignment centered with max-width 1000px. Make it possible to test this alignment with virtual guides object by using corrections

####Approximation
How to define custom approximations

####Absent elements
Sometimes we hide something for mobile users. Lets explain that to Galen properly

####Javascript injections and cookie handling
Implement tests for hidden components using js injection (to make stuff visible on page).
FeatureSwitches handling with cookies

####Selenium interaction 1
wait for page to build. There might be some delays in javascript for a DHTML app so lets try to handle it with javascript runner.
    
####Selenium interaction 2
Need to login to your profile page? Lets take over the browser with javascript runner

####More checks
* spec on   (e.g. price label on top of image)
* spec centered  (e.g. caption inside image block)
* spec aligned

####Text verification
Sometimes you want to verify text inside elements on page.

####Componenent testing
What if we have multiple components on the same page? (e.g. comments, search results etc)

####Conditional blocks
Don't know which exact element to expect?

####TTD for Responsive Design
Still need to figure out something for this one. Maybe we could perform an experiment where frontend developers would implement a page based on galen specs and then we could compare the outcome with original sketch.

