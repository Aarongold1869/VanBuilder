(this["webpackJsonpvanbuilder-react"]=this["webpackJsonpvanbuilder-react"]||[]).push([[0],{16:function(e,n,t){},17:function(e,n,t){},19:function(e,n,t){"use strict";t.r(n);var a=t(1),c=t.n(a),i=t(7),s=t.n(i),r=(t(16),t(17),t(0));var o=function(){return Object(r.jsx)("div",{className:"App",children:Object(r.jsxs)("header",{className:"App-header",children:[Object(r.jsxs)("p",{children:["Edit ",Object(r.jsx)("code",{children:"src/App.js"})," and save to reload."]}),Object(r.jsx)("a",{className:"App-link",href:"https://reactjs.org",target:"_blank",rel:"noopener noreferrer",children:"Learn React"})]})})},l=function(e){e&&e instanceof Function&&t.e(3).then(t.bind(null,20)).then((function(n){var t=n.getCLS,a=n.getFID,c=n.getFCP,i=n.getLCP,s=n.getTTFB;t(e),a(e),c(e),i(e),s(e)}))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));var d=t(11),u=t(9),j=t(10),b=t(6);function h(e,n,t,a){var c;a&&(c=JSON.stringify(a));var i=new XMLHttpRequest,s="http://localhost:8000/api".concat(n);i.responseType="json";var r=function(e){var n=null;if(document.cookie&&""!==document.cookie)for(var t=document.cookie.split(";"),a=0;a<t.length;a++){var c=t[a].trim();if(c.substring(0,e.length+1)===e+"="){n=decodeURIComponent(c.substring(e.length+1));break}}return n}("csrftoken");i.open(e,s),i.setRequestHeader("Content-Type","application/json"),r&&(i.setRequestHeader("X-Requested-With","XMLHttpRequest"),i.setRequestHeader("X-CSRFToken",r)),i.onload=function(){403===i.status&&("Authentication credentials were not provided."===i.response.detail&&-1===window.location.href.indexOf("login")&&(window.location.href="/login?showLoginRequired=true"));t(i.response,i.status)},i.onerror=function(e){t({message:"The request was an error"},400)},i.send(c)}function m(){var e=Object(a.useState)([]),n=Object(u.a)(e,2),t=n[0],c=n[1],i=Object(a.useState)(!1),s=Object(u.a)(i,2),o=s[0],l=s[1];return Object(a.useEffect)((function(){if(!1===o){h("GET","/build/list/",(function(e,n){200===n?(c(e),l(!0)):alert("There was an error")}))}}),[o,l]),Object(r.jsx)("div",{children:t.map((function(e,n){return Object(r.jsx)(f,{build:e},"".concat(n,"-{item.id}"))}))})}function f(e){var n=e.build;return Object(r.jsx)("div",{className:"mt-3",children:Object(r.jsxs)(b.a,{border:"salmon",children:[Object(r.jsx)(b.a.Header,{children:n.build_title}),Object(r.jsxs)(b.a.Body,{children:[Object(r.jsx)(b.a.Title,{children:n.vehicle_info}),Object(r.jsxs)(b.a.Text,{children:["Budget: $",n.budget]}),Object(r.jsx)(j.a,{variant:"bluegreen",onClick:function(e){e.preventDefault(),window.location.href="build/".concat(n.id,"/components/")},children:"View Build"})]})]})})}function v(e){return Object(r.jsx)("div",{className:e.className,children:Object(r.jsx)(m,Object(d.a)({},e))})}var g=t.p+"static/media/Logo.fc55694e.png",p=t.p+"static/media/arrowButton.34c4bd34.svg";function O(e){return Object(r.jsxs)("div",{className:"centered",children:[Object(r.jsx)("img",{className:"main-logo",src:g,alt:"van builter logo"}),Object(r.jsxs)("div",{className:"btn-group",children:[Object(r.jsxs)("a",{className:"arrow-btn",onClick:function(e){e.preventDefault(),window.location.href="builds"},children:["Start Building",Object(r.jsx)("img",{src:p})]}),Object(r.jsxs)("a",{className:"arrow-btn",onClick:function(e){e.preventDefault(),window.location.href="login"},children:["Login / Signup",Object(r.jsx)("img",{src:p})]})]})]})}var x=t.p+"static/media/Logo-white-text.2e65ba81.png";function w(e){return Object(r.jsxs)("nav",{id:"navbar",className:"navbar",children:[Object(r.jsx)("a",{className:"logo-link",alt:"vanbuilder.com logo",href:"#home",children:Object(r.jsx)("img",{id:"nav-logo",className:"nav-logo",src:x})}),Object(r.jsxs)("ul",{id:"nav-list",className:"nav-list",children:[Object(r.jsx)("li",{className:"nav-list-item",children:Object(r.jsx)("a",{classname:"nav-link",href:"#builds",children:"Builds"})}),Object(r.jsx)("li",{className:"nav-list-item",children:Object(r.jsx)("a",{classname:"nav-link",href:"#components",children:"Components"})}),Object(r.jsx)("li",{className:"nav-list-item",children:Object(r.jsx)("a",{classname:"nav-link",href:"#about",children:"About"})}),Object(r.jsx)("li",{className:"nav-list-item",children:Object(r.jsx)("a",{classname:"nav-link",href:"#contact",children:"Contact"})}),Object(r.jsx)("li",{className:"nav-list-item",children:Object(r.jsx)("a",{classname:"nav-link",href:"#profile",children:"Profile"})})]})]})}var k=document.getElementById("root");k&&s.a.render(Object(r.jsx)(o,{}),k);var N=c.a.createElement;document.querySelectorAll(".navbar").forEach((function(e){s.a.render(N(w,e.dataset),e)})),document.querySelectorAll(".landing-page").forEach((function(e){s.a.render(N(O,e.dataset),e)})),document.querySelectorAll(".build-list").forEach((function(e){s.a.render(N(v,e.dataset),e)})),l(),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[19,1,2]]]);
//# sourceMappingURL=main.e2c6a3d0.chunk.js.map