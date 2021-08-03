#!/usr/bin/node

exports.esrever = function (list) {
  return list.map((val, index, list)=>{return list[list.length - index - 1];});
};
