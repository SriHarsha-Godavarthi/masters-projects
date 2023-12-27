# what react is all about?
1. display html.
2. changes that html when ever user does something.
# how do we tell react to show html?
-> By returning jsx from react components.
# what is a react component?
-> functions that return JSX (that look similar to HTML).
-> It tells what to show on screen. there can me many components for small app.

**when a tag has the capital letter at starting react assumes it as Component and shows jsx inside that Component.if not it should be html element.

# how react works?
-> all js files are converted to single bundle.js file which placed on the server.and server also will have index.html file which returns on client request returned to user as response and loaded and executed.

# install nodeJS from (https://nodejs.org/en)
# how to create react app
-> npx create-react-app <appName>
browser doesn't understand JSX
Babel - convert jsx into javascript 
webpack - merge all files into single file(bundle.js)

# props (imp)
1. all html properties has to be camelCase
2. constants can be passed directly with in curlybraces
3. boolean true can directly pass property name for false we have to pass value
4. inline-styling we have to pass object inside curlybraces
5. class property in html can be used as className
 

