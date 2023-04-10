### 1. jest에서 외부 모듈을 테스트 하기 위해서 아래의 패키지 설치가 필요함
- @babel/core
- @babel/preset-env
- @babel/plugin-transform-modules-commonjs
- @babel/plugin-transform-runtime
- 설치예시) npm i -D @babel/core

### 2. ROOT 폴더에 babel.config.js 파일을 생성 및 다음 내용 적기
```javascript
module.exports = {
  presets: ["@babel/preset-env"],
  env: {
    test: {
      plugins: [
        '@babel/plugin-transform-modules-commonjs',
        '@babel/plugin-transform-runtime'
      ]
    }
  }
}
```