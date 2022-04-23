var a, b, c;
console.log("HI im calculator maked by D-BOY");
console.log("\nChoose what you want to do\n1 - Add\n2 - Subtract\n3 - Divide\n4 - Multiply\n5 - Spoteng\n");
a = Number.parseInt(input("Choose: "));

if (a === 1) {
  b = Number.parseInt(input("Number 1: "));
  c = Number.parseInt(input("Number 2: "));
  console.log("the result is : " + (b + c).toString());
} else {
  if (a === 2) {
    b = Number.parseInt(input("Number 1: "));
    c = Number.parseInt(input("Number 2: "));
    console.log("the result is: " + (b - c).toString());
  } else {
    if (a === 3) {
      b = Number.parseInt(input("Number 1: "));
      c = Number.parseInt(input("Number 2: "));
      console.log("the result is: " + Number.parseInt(b / c).toString());
    } else {
      if (a === 4) {
        b = Number.parseInt(input("Number 1: "));
        c = Number.parseInt(input("Number 2: "));
        console.log("the result is: " + (b * c).toString());
      } else {
        if (a === 5) {
          b = Number.parseInt(input("Number 1: "));
          c = Number.parseInt(input("Number 2: "));
          console.log("the result is: " + Math.pow(b, c).toString());
        }
      }
    }
  }
}
