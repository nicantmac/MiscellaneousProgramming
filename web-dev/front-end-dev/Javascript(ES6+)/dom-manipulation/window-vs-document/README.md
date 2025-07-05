# Window vs Document in JavaScript

#### What is `window`?
- Represents the browser window/tab
- Global scope in JS

#### What is `document`?
- Represents the loaded HTML DOM
- Part of `window`

### Key Differences
| Feature         | window           | document        |
|-----------------|------------------|-----------------|
| Global object   | ✅              | ❌              |
| DOM access      | ❌              | ✅              |
| Methods         | alert(), scrollTo() | getElementById(), querySelector() |

## Example
```js
console.log(window.innerWidth);
console.log(document.title);
