def hanoi(n, source, auxiliary, target, towers):
    if n == 1:
        # Перемістити диск з source на target
        disk = towers[source].pop()
        towers[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {towers}")
    else:
        # Перемістити n-1 дисків з source на auxiliary, використовуючи target як допоміжний
        hanoi(n - 1, source, target, auxiliary, towers)
        
        # Перемістити найбільший диск з source на target
        disk = towers[source].pop()
        towers[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {towers}")
        
        # Перемістити n-1 дисків з auxiliary на target, використовуючи source як допоміжний
        hanoi(n - 1, auxiliary, source, target, towers)

def main():
    n = int(input("Введіть кількість дисків: "))
    towers = {
        'A': list(range(n, 0, -1)),  # Початкове заповнення стрижня A
        'B': [],
        'C': []
    }
    print(f"Початковий стан: {towers}")
    hanoi(n, 'A', 'B', 'C', towers)
    print(f"Кінцевий стан: {towers}")

if __name__ == "__main__":
    main()
