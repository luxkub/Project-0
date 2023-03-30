# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](c) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Winnie Kubuanu](ekubuanu@uncc.edu)
* [Zachary Turnmire](zturnmir@uncc.edu)
* [Mack Larson](mmailto:email@uncc.edu)

## Revisions

When a change is made to the document, a new revision should be created. The revision should be added to the table below with all information filled out.

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [Winnie Kubuanu](ekubuanu@uncc.edu) | [Winnie Kubuanu](ekubuanu@uncc.edu) |


## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

## Introduction

In this section, you should give a brief overview of what your project will be. Describe the software system you are building and what problems it solves. You should also give a short description of the stakeholders (users of the system) and what their needs are. There is no set formatting requirement, but you should maintain a consistent structure across future sections. Not all members must contribute to this section.

## Requirements

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:

* **ID:** REQ-4.
  * **Description:** A search function that makes it simple and quick for users to find content should be available on the website.
  * **Type:** `Functional`
  * **Priority:** 1
  * **Rationale:** A search function helps users quickly find the content they're looking for instead of navigating through numerous pages or menus.
  * **Testing:** You can test the functionality of the search function by entering a search query.

* **ID:** REQ-5
  * **Description:** A shopping cart function that enables users to add things they want to buy and determine the total cost of their transaction should be available on the website store.
  * **Type:** `Functional`
  * **Priority:** 2
  * **Rationale:** By enabling customers to quickly buy multiple items at once rather than having to check out each item separately, a shopping cart feature can boost sales.
  * **Testing:** You can test a shopping cart function by adding products, changing quantities, and removing items.

* **ID:** REQ-6
  * **Description:** The website's content should be easy to read and understand.
  * **Type:** `Functional`
  * **Priority:** 2
  * **Rationale:** Content that is simple to read and understand has a higher chance of generating user engagement. Users may become annoyed and leave the website if the material is unclear, hard to understand, or full of jargon, which can have an effect on engagement and conversions.
  * **Testing:** We may test this by asking a group of visitors to read the website's content and offer feedback on the text's clarity and readability.

## Constraints

Project Requirements: The website must be aesthetically pleasing  which can be difficult when there are few design resources available.

Language Constraint: For this project we are limited to using Python and Flask.

## Use Cases

* **ID:** UC-3
  * **Description:** The user can start the checkout procedure, which entails providing their billing and shipping information, choosing a payment option, and reviewing their order specifics before completing the transaction.
  * **Actors:** The customer
  * **Preconditions:** The user has added an item to their cart, entered their shipping and billing information, their payment method, and submitted their payment.
  * **Postconditions:** In an online web store, processing the customer's shipping label and sending the order to the shipping carrier are among the postconditions of the checkout use case. The store may also create an order confirmation page and send the user an email of confirmation, update its inventory system, or update its inventory system. 

  * **ID:** UC-4
  * **Description:** A user can click on a single product to view more information, including a description.
  * **Actors:** The customer
  * **Preconditions:** The user has added an item to their cart, entered their shipping and billing information, their payment method, and submitted their payment.
  * **Postconditions:** The postconditions of the "search and browse products" use case would be the user being shown a list of products based on their search query. 

## User Stories

* **ID:** US-3
  * **Type of User:** `Customer`
  * **Description:** Johnny wants to quickly find the games he wants on our online store. Without encountering any navigational difficulties or technical difficulties, he plans to travel to the homepage of the online store, look for the items and add them to his cart. He will be happy with the online shopping experience and intends to return to the website for additional purchases if she can quickly and simply find all the items he wants.

  * **ID:** US-4
  * **Type of User:** `Customer`
  * **Description:** Tomas, a dedicated gamer, wants to browse the online store's assortment of video games fast and conveniently, view in-depth information on each game, and buy it. He anticipates a quick and easy checkout experience and intends to come back for additional purchases.

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Term:** Function
  * **Definition:** A function is a website's ability to complete a particular task.
