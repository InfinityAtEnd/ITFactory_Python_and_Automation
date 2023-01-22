Feature: Test the search functionality in the homepage of Ebay

  Background:
    Given Home page: I am on Ebay homepage

  @Tag01 @TagALL #tags for scenario individual run or all of them
  Scenario Outline: Check that the user can make a simple search in the Ebay homepage
    When Home page: I search for "<product>" from category "<category>"
    Then Home page: I have at least "<results>" results returned
    @electronics
    Examples:
      | product | category                  | results |
      | iphone  | Cell Phones & Accessories | 1000    |
      | tv      | Consumer Electronics      | 20000   |


    @clothes
    Examples:
      | product | category                      | results |
      | sweter  | Clothing, Shoes & Accessories | 1000000 |

    @baby
    Examples:
      | product | category | results |
      | pampers | Baby     | 300     |

  @Tag02 @TagALL #tags for scenario individual run or all of them
  Scenario Outline: Check that the user can make an advanced search for a product
    When Home page: When I click on the advanced link
    When Advanced search page: I type "<product>" in the enter keyword textbox
    When Advanced search page: I select Exact words exact order from keyword options
    When Advanced search page: I choose "<category>" from the category list
    When Advanced search page: I type "<exclude_product>" in exclude words from your search
    When Advanced search page: I click search button
    Then Home page: I have at least "<results>" results returned
    @electronics
    Examples:
      | product | category                  | exclude_product | results |
      | iphone  | Cell Phones & Accessories | iphone9         | 1000    |
      | tv      | Consumer Electronics      | cable           | 100000  |


    @clothes
    Examples:
      | product | category                      | exclude_product | results |
      | sweter  | Clothing, Shoes & Accessories | women           | 300     |

    @baby
    Examples:
      | product | category | exclude_product | results |
      | pampers | Baby     | sample          | 300     |

  @Tag03
  Scenario Outline: Check that the user can add a product to shopping cart
    When Home page: I search for "<product_name>" from category "<category_name>"
    When Search Results: I choose the first product in the list
    When Search Results: I choose "<property01>" as "<value01>"
    When Search Results: I choose "<property02>" as "<value02>"
    When Search Results: I choose "<property03>" as "<value03>"
    When Search Results: I choose "<property04>" as "<value04>"
    When Search Results: I click Add to Cart button
    When Search Results: I click on the shopping cart
    Then Shopping Cart: I have one product in the shopping cart


    @electronics
    Examples:
      | product_name           | category_name                 | property01  | value01            | property02 | value02                           | property03 | value03 | property04 | value04 |
      | iphone max 11 pro 2011 | Cell Phones & Accessories     | Phone Model | For Iphone 12 Mini | Design     | D2012 Jack Skull Nightmare Bef... | None       | None    | None       | None    |
      | blouse                 | Clothing, Shoes & Accessories | Color       | white              | Size       | XL                                | None       | None    | None       | None    |