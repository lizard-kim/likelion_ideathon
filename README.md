# Like Lion Ideathon

## Intro

 멋쟁이 사자처럼 중앙 아이디어톤 웹페이지 개발 프로젝트

## Installation (OS X, Linux)

<code>$ cd likelion_ideathon</code>
<code>$ pip install -r requirements.txt </code>

## Sass/Scss Manual

각 app안에 static 폴더를 만들어, 그안에 scss file을 생성하면 됩니다.

templates의 html file과 연결하는 방법은 아래와 같습니다!

```html
<!DOCTYPE html>
{% load sass_tags %}
<html>
<head>
  <title>Like Lion Ideathon</title>
  <link href="{% sass_src 'style/about.scss' %}" rel="stylesheet" type="text/css"/> 
</head>
<body>
    <h1> this is about </h1>
</body>
</html>
```

> 문서 최상위에 {% load sass_tags %} 를 입력하여 sass file을 가져와 줍니다.
>
> 다음, <code> link href="{% sass_src 'style/about.scss' %}" rel="stylesheet" type="text/css" </code> 를 통해 내가 만든 scss file을 연결해줍시다.
>
> 만약 static/style/about.scss 의 파일트리가 아닌, static/about.scss의 파일트리를 사용했다면, <code>link href="{% sass_src 'about.scss' %}" rel="stylesheet" type="text/css"</code> 이렇게 사용해주면 되겠죠?

## Workflow for Collaboration

Link: [workflow_manual](./Workflow.md)

## Contributors

- 김태영
- 박종현
- 박지형
- 신효경
- 최광일
- 박종현(제일 잘생김)



