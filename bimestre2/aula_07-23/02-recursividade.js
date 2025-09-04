function faz(n) {
    console.log("oi "+n)
    // if (n > 20000) {
    //     return
    // }
    faz(n + 1)
    console.log("tchau "+n)
}

faz(1)
