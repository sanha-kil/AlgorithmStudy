var obj = {
  name: 'B',
  print: function () {
    var inner1 = function () {
      console.log(this.name, name);
    };
    inner1();

    var inner2 = () => console.log(this.name, name);
    inner2();

    var name = 'C';
    console.log(this.name, name);
  },
};

function a() {
  obj.print();
}

function b() {
  var name = 'D'
  a()
}

b()