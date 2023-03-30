# Software Requirements Specification Document

## Group Members

* [Winnie Kubuanu](mailto:ekubuanu@uncc.edu)
* [Mack Larson](mailto:clarson9@uncc.edu)

## Revisions

When a change is made to the document, a new revision should be created. The revision should be added to the table below with all information filled out.

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [David Gary](mailto:dgary9@uncc.edu) | [David Gary](mailto:dgary@uncc.edu) |
|1.0| 03/30/23 | Initial Document | [Mack Larson](mailto:clarson9@uncc.edu) | [Mack Larson](mailto:clarson9@uncc.edu) |
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


* **REQ-7:** Video game Object
  * **Description:** A Video game Object that stores a Price, a inventory size, A image, and the name of the Video game
  * **Type:** Functional
  * **Priority:** 3
  * **Rationale:** This requirement stores inventory, as well as the display capabilities and prices
  * **Testing:** We would write tests to check price, inventory, and images.  

* **REQ-8:** Checkout
  * **Description:** A Checkout process where a person can buy the items in their shopping cart
  * **Type:** Functional
  * **Priority:** 1
  * **Rationale:** The people need to be able to buy whatever they want to get from the stole
  * **Testing:** We would write tests to check that inventory decreases, the customer gets their card charged, and the shopping cart gets emptied

* **REQ-9:** Error Messages
  * **Description:** Clear and consise error messages to tell the client what they did wrong
  * **Type:** Functional
  * **Priority:** 5
  * **Rationale:** These error messages would help the client know what they should do right.
  * **Testing:** We would write tests to check error messages are thrown when someone enters something we dont want into a field  

* **REQ-4** Searching
  * **Description:** A search function that makes it simple and quick for users to find content should be available on the website.
  * **Type:** `Functional`
  * **Priority:** 1
  * **Rationale:** A search function helps users quickly find the content they're looking for instead of navigating through numerous pages or menus.
  * **Testing:** You can test the functionality of the search function by entering a search query.

* **REQ-5:** Shopping Cart
  * **Description:** A shopping cart function that enables users to add things they want to buy and determine the total cost of their transaction should be available on the website store.
  * **Type:** `Functional`
  * **Priority:** 2
  * **Rationale:** By enabling customers to quickly buy multiple items at once rather than having to check out each item separately, a shopping cart feature can boost sales.
  * **Testing:** You can test a shopping cart function by adding products, changing quantities, and removing items.

* **REQ-6** Accessibility
  * **Description:** The website's content should be easy to read and understand.
  * **Type:** `Functional`
  * **Priority:** 2
  * **Rationale:** Content that is simple to read and understand has a higher chance of generating user engagement. Users may become annoyed and leave the website if the material is unclear, hard to understand, or full of jargon, which can have an effect on engagement and conversions.
  * **Testing:** We may test this by asking a group of visitors to read the website's content and offer feedback on the text's clarity and readability.

## Constraints

Project Requirements: The website must be aesthetically pleasing  which can be difficult when there are few design resources available.

Language Constraint: For this project we are limited to using Python and Flask.

Real: We are constraned by real-world applications 

Video games: We are constraned to only selling video game objects because this is a video game store
## Use Cases

* **UC-3:** 
  * **Description:** The user can start the checkout procedure, which entails providing their billing and shipping information, choosing a payment option, and reviewing their order specifics before completing the transaction.
  * **Actors:** The customer
  * **Preconditions:** The user has added an item to their cart, entered their shipping and billing information, their payment method, and submitted their payment.
  * **Postconditions:** In an online web store, processing the customer's shipping label and sending the order to the shipping carrier are among the postconditions of the checkout use case. The store may also create an order confirmation page and send the user an email of confirmation, update its inventory system, or update its inventory system. 

* **UC-5:** Checkout
  * **Description:** A person should be able to use the checkout process to buy the items in their cart
  * **Actors:** Customer
  * **Preconditions:** Shopping cart isn't empty, they have a valid card, and the items they want arent out of stock
  * **Postconditions** Shopping cart gets emptied, card gets charged, inventory gets decreased. 

* **UC-6:** Add video game object
  * **Description:** The ability to add a new video game product to the store
  * **Actors:** Admin
  * **Preconditions:** More then zero of the item you're trying to add, and the information for the fields
  * **Postconditions** A new item added to the store, along with description, price, and name. 

* **UC-4:** View more info
  * **Description:** A user can click on a single product to view more information, including a description.
  * **Actors:** The customer
  * **Preconditions:** The user has added an item to their cart, entered their shipping and billing information, their payment method, and submitted their payment.
  * **Postconditions:** The postconditions of the "search and browse products" use case would be the user being shown a list of products based on their search query. 

## User Stories

* **US-3:** Johnny
  * **Type of User:** `Customer`
  * **Description:** Johnny wants to quickly find the games he wants on our online store. Without encountering any navigational difficulties or technical difficulties, he plans to travel to the homepage of the online store, look for the items and add them to his cart. He will be happy with the online shopping experience and intends to return to the website for additional purchases if she can quickly and simply find all the items he wants.

* **US-5:** Checking Out of Store
  * **Type of User:** Customer
  * **Description:** I want to be able to go ahead and buy whatever is in my shopping cart once im done browsing

* **US-6:** Adding new inventory to the store
  * **Type of User:** Admin
  * **Description:** I would like to be able to add new types of product to my store

* **US-4:** Tomas
  * **Type of User:** `Customer`
  * **Description:** Tomas, a dedicated gamer, wants to browse the online store's assortment of video games fast and conveniently, view in-depth information on each game, and buy it. He anticipates a quick and easy checkout experience and intends to come back for additional purchases.

## Glossary

* **Term:** Attribute
  * **Definition:** A field that contains info, mainly used in objects. 
* **Term:** Function
  * **Definition:** A function is a website's ability to complete a particular task.
