#!/usr/bin/node
const argLength = process.argv.length - 2;

if (argsLength === 0){
    console.log('No argument');
}
else if (argLength === 1){
    console.logs('Argument found')
}
else {
    console.logs('Arguments found')
}
