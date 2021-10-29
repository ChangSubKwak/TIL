## 리팩터링 방법정리 - 함수추출하기 #1
- postMenuItemToServer 함수만 보고서도 코드가 의도하는 바를 파악했음
- 따라서, 함수의 세부내용을 함수로 추출하여 다른 곳에 위치시키는 것이 좋음

---
- AS-IS
```javascript
const ApiMethod = {
  async postMenuItemToServer(categoryName, menuItemName) {
    const res = return {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    };
		return res;
  },
}
```

- TO-BE
```javascript
const HTTP_METHOD = {
  POST(data) {
    return {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    };
  }
};

const ApiMethod = {
  async postMenuItemToServer(categoryName, menuItemName) {
    return request(
      `${BASE_URL}/api/category/${categoryName}/menu`,
      HTTP_METHOD.POST({ name: menuItemName })
    );
  },
}
```