function rank(vit, derr) {
    if (saldo(vit, derr) < 10) {
        return "Ferro";
    } else if (10 < saldo(vit, derr) && saldo(vit, derr) <= 20) {
        return "Bronze";
    } else if (20 < saldo(vit, derr) && saldo(vit, derr) <= 50) {
        return "Prata";
    } else if (50 < saldo(vit, derr) && saldo(vit, derr) <= 80) {
        return "Ouro";
    } else if (80 < saldo(vit, derr) && saldo(vit, derr) <= 90) {
        return "Diamante";
    } else if (90 < saldo(vit, derr) && saldo(vit, derr) <= 100) {
        return "Lendário";
    } else if (saldo(vit, derr) > 100) {
        return "Imortal";
    }
}

function saldo(x, y) {
    return x - y;
}

while (true) {
    var vit = parseInt(prompt("Quantas vitórias você possui? "));
    var derr = parseInt(prompt("Quantas derrotas você possui? "));
    console.log(`O Herói tem saldo de ${saldo(vit, derr)} e está no nível de ${rank(vit, derr)}`);
    var resp = prompt("Quer adicionar outro personagem? [S/N]").trim();
    if (!resp.toLowerCase().startsWith('n')) {
        continue;
    } else {
        break;
    }
}
