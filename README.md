# DB-Assignment
**Solution 1:** Based on the provided context, the "Product" and "Product_Category" entities have a relationship defined by the "category_id" column in the "Product" entity. Each product is associated with a specific product category, and this relationship is established through the "category_id" column, which is an integer that corresponds to the "id" of a particular category in the "Product_Category" entity.

**Solution 2:** To ensure that each product in the "Product" table has a valid category assigned to it, you can implement the following methods:
  i)  Foreign Key Constraint
  ii) Trigger Function
