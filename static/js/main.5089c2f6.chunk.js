(this["webpackJsonpvanbuilder-react"]=this["webpackJsonpvanbuilder-react"]||[]).push([[0],{10:function(e,t,n){},11:function(e,t,n){},13:function(e,t,n){"use strict";n.r(t);var a=n(1),c=n.n(a),i=n(2),s=n.n(i),r=(n(10),n(11),n(0));var l=function(){return Object(r.jsx)("div",{className:"App",children:Object(r.jsxs)("header",{className:"App-header",children:[Object(r.jsxs)("p",{children:["Edit ",Object(r.jsx)("code",{children:"src/App.js"})," and save to reload."]}),Object(r.jsx)("a",{className:"App-link",href:"https://reactjs.org",target:"_blank",rel:"noopener noreferrer",children:"Learn React"})]})})},o=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,14)).then((function(t){var n=t.getCLS,a=t.getFID,c=t.getFCP,i=t.getLCP,s=t.getTTFB;n(e),a(e),c(e),i(e),s(e)}))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));var d=n(5),u=n(4);function j(e,t,n,a){var c;a&&(c=JSON.stringify(a));var i=new XMLHttpRequest,s="http://localhost:8000/api".concat(t);i.responseType="json";var r=function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),a=0;a<n.length;a++){var c=n[a].trim();if(c.substring(0,e.length+1)===e+"="){t=decodeURIComponent(c.substring(e.length+1));break}}return t}("csrftoken");i.open(e,s),i.setRequestHeader("Content-Type","application/json"),r&&(i.setRequestHeader("X-Requested-With","XMLHttpRequest"),i.setRequestHeader("X-CSRFToken",r)),i.onload=function(){403===i.status&&("Authentication credentials were not provided."===i.response.detail&&-1===window.location.href.indexOf("login")&&(window.location.href="/login?showLoginRequired=true"));n(i.response,i.status)},i.onerror=function(e){n({message:"The request was an error"},400)},i.send(c)}function b(){var e=Object(a.useState)([]),t=Object(u.a)(e,2),n=t[0],c=t[1],i=Object(a.useState)(!1),s=Object(u.a)(i,2),l=s[0],o=s[1];return Object(a.useEffect)((function(){if(!1===l){j("GET","/build/list/",(function(e,t){200===t?(c(e),o(!0)):alert("There was an error")}))}}),[l,o]),Object(r.jsx)("div",{className:"build-list-container",children:n.map((function(e,t){return Object(r.jsx)(h,{build:e},"".concat(t,"-{item.id}"))}))})}function h(e){var t=e.build;return console.log(t),Object(r.jsx)("div",{className:"build-list-item",onClick:function(e){e.preventDefault(),window.location.href="/builds/".concat(t.id,"/")},children:Object(r.jsxs)("div",{className:"build-list-item-content",children:[Object(r.jsxs)("div",{className:"build-list-item-content-text",children:[Object(r.jsx)("h3",{children:t.build_title}),Object(r.jsxs)("p",{children:["Van:\u2003",t.vehicle_info]}),Object(r.jsxs)("p",{children:["Budget:\u2003$",t.budget]}),Object(r.jsxs)("p",{children:["Last Updated:\u2003",t.last_updated]})]}),Object(r.jsx)("img",{src:t.image})]})})}var m=n.p+"static/media/arrowButton.34c4bd34.svg";function f(e){return Object(r.jsxs)("div",{className:"centered",style:{marginTop:"20vh"},children:[Object(r.jsxs)("div",{className:"build-list-view-title",children:[Object(r.jsx)("h1",{children:"Your Builds"}),Object(r.jsxs)("a",{className:"arrow-btn",onClick:function(e){e.preventDefault(),window.location.href="/builds/new-build/"},children:["Start New Build",Object(r.jsx)("img",{src:m})]})]}),Object(r.jsx)("hr",{}),Object(r.jsx)(b,Object(d.a)({},e))]})}var v=n.p+"static/media/Logo.fc55694e.png";function p(e){return Object(r.jsxs)("div",{className:"centered",children:[Object(r.jsx)("img",{className:"main-logo",src:v,alt:"van builter logo"}),Object(r.jsxs)("div",{className:"btn-group",children:[Object(r.jsxs)("a",{className:"arrow-btn",onClick:function(e){e.preventDefault(),window.location.href="builds"},children:["Start Building",Object(r.jsx)("img",{src:m})]}),Object(r.jsxs)("a",{className:"arrow-btn",onClick:function(e){e.preventDefault(),window.location.href="login"},children:["Login / Signup",Object(r.jsx)("img",{src:m})]})]})]})}var O=n.p+"static/media/Logo-white-text.2e65ba81.png";function g(e){return Object(r.jsxs)("nav",{id:"navbar",className:"navbar",children:[Object(r.jsx)("a",{className:"logo-link",alt:"vanbuilder.com logo",href:"#home",children:Object(r.jsx)("img",{id:"nav-logo",className:"nav-logo",src:O})}),Object(r.jsxs)("ul",{id:"nav-list",className:"nav-list",children:[Object(r.jsx)("li",{className:"nav-list-item",children:Object(r.jsx)("a",{classname:"nav-link",href:"#builds",children:"Builds"})}),Object(r.jsx)("li",{className:"nav-list-item",children:Object(r.jsx)("a",{classname:"nav-link",href:"#components",children:"Components"})}),Object(r.jsx)("li",{className:"nav-list-item",children:Object(r.jsx)("a",{classname:"nav-link",href:"#about",children:"About"})}),Object(r.jsx)("li",{className:"nav-list-item",children:Object(r.jsx)("a",{classname:"nav-link",href:"#contact",children:"Contact"})}),Object(r.jsx)("li",{className:"nav-list-item",children:Object(r.jsx)("a",{classname:"nav-link",href:"#profile",children:"Profile"})})]})]})}var x=document.getElementById("root");x&&s.a.render(Object(r.jsx)(l,{}),x);var w=c.a.createElement;document.querySelectorAll(".navbar").forEach((function(e){s.a.render(w(g,e.dataset),e)})),document.querySelectorAll(".landing-page").forEach((function(e){s.a.render(w(p,e.dataset),e)})),document.querySelectorAll(".build-list").forEach((function(e){s.a.render(w(f,e.dataset),e)})),o(),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[13,1,2]]]);
//# sourceMappingURL=main.5089c2f6.chunk.js.map