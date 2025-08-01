export function factorial(n) {
    if (n < 0) {
        throw new Error("Factorial is not  for negative numbers");
    }
    if (n === 0 || n === 1) {
        return 1;
    }
    return n * factorial(n - 1);
}