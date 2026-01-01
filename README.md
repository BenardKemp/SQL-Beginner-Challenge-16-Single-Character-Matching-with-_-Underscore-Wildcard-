# SQL Beginner Challenge #16: Single-Character Matching with `_`

**Difficulty:** Beginner  
**Estimated time:** 10–15 minutes  
**Concepts:** `LIKE`, `_` (underscore wildcard), precise pattern matching  

This challenge introduces the underscore (`_`) wildcard, which matches **exactly one character** in SQL pattern matching.

---

## 🧠 The Problem

A product manager asks:

> “Can we find products whose SKU follows a very specific pattern, where only **one character varies**?”

You already know `%` matches any number of characters.  
In this challenge, you’ll use `_` to match **exactly one character**.

---

## 📊 Table Schema

### `products`

| Column Name | Type | Description |
|------------|------|-------------|
| product_id | INTEGER | Unique product ID |
| name | TEXT | Product name |
| sku | TEXT | Product SKU |
| price | DECIMAL | Product price |

---

## 🧪 Sample Data

| product_id | name | sku | price |
|-----------:|------|-----|------:|
| 201 | USB-C Hub | USB1-A | 34.50 |
| 202 | USB-C Hub Pro | USB2-A | 49.99 |
| 203 | USB Flash Drive | USB10-A | 19.99 |
| 204 | Wireless Mouse | MOU1-B | 24.99 |
| 205 | Mechanical Keyboard | KEY1-B | 89.00 |

---

## ✅ Requirements

Your query must:

- Return:
  - `name`
  - `sku`
- Match SKUs that follow this pattern:

