#!/usr/bin/node
exports.esrever = (list) => {
  const list_ = [];
  for (let i = 0; i < list.length; i++) {
    list_.unshift(list[i]);
  }
  return list_;
};
