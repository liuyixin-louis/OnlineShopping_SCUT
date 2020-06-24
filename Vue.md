# Vue 快速入门

## 组件

1. **子组件只能在父组件的template中使用。**

> 两种错误方式：
>
> 1. **以子标签的形式在父组件中使用**
> 2. **在父组件标签外使用子组件**

2. **使用Vue.component()直接创建和注册组件**

> ```vue
> // 全局注册，my-component1是标签名称
> Vue.component('my-component1',{
> 	template: '<div>This is the first component!</div>'
> })
> 
> var vm1 = new Vue({
> 	el: '#app1'
> })
> ```

3. 父组件和子组件的属性props感知域一致

![image](https://images2015.cnblogs.com/blog/341820/201606/341820-20160629071700437-2088181944.png)

