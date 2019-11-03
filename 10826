#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define HASHFUNC(a, b) (((reinterpret_cast<unsigned __int64>(a)) * 27644437) % (b)) // перевод в 64 бита, умножение на большое простое число и остаток от деления на размер таблицы (не идеальный алгоритм, чувствительный к размеру таблицы (для этого размер - простое число))

struct T;
typedef Vector <T*> ListT;

struct HashInfo              // ячейка
{
    __int64 kod_;
    T * t_;
    union
    {
        __int64 i_;
        T * u_;
    };
};

struct HashTable             // таблица
{
    HashInfo data_[N+5];     // data + 5 (запас)
    __int64 kod_;            // занятость
    int v_;                  // count

    HashTable();                            // обнуление памяти
    inline void Clear() { kod_++; v_ = 0; } // очистить всё (вместо обнуления большого куска памяти используется увеличение глобальной переменной занятости ячейки на 1)
    HashInfo * Find(T * a);                 // найти элемент
    void Add(T * a, __int64 d = 0);         // добавить элемент
    void Del(T * a);                        // удалить элемент
};

template<int N>
void HashTable<N>::Del(T * a)
{
    int n = -1
    for (int i = HASHFUNC(a, N); data_[i].kod_ == kod_; i++) // поиск элемента (если не найден, то break)
        if (data_[i].t_ == a)
        {
            n = i;
            break
        }
    if (n < 0) return;
    for (int j = n + 1; date_[j].kod_; j++) // Исправление таблицы (из-за коллизии)
    {
        int hh = HASHFUNC(date_[j].t_, N);
        if (hh <= n)
        {
            data_[n] = data_[j];
            n = j;
        }
    }
    data_[n].kod_ = 0;
    v_--
}

template<int N>
void HashTable <N> ::Add(T * a, __int64 d)  // добавление элемента
{
    int j;
    for (j = HASHFUNC(a, N); data_[j].kod_ == kod_; j++); // поиск свободной ячейки
    if (j >= N + 4) Error(L"Таблица переполнена"); // проверка на переполнение конца таблицы (если коллизия в конце)
    data_[j].t_ = a;
    data_[j].kod_ = kod_;
    data_[j].i_ = d;
    v_++;
    if (v_ * 1.5 > N) Error(L"Маленькая таблица"); // проверка на переполнение (если больше, чем 2/3 таблицы заполнено)
}

template<int N>
HashInfo * HashTable<N>::Find(T * a) // поиск (если элемент найден, то вернуть его указатель, иначе - 0)
{
    for (int i = HASHFUNC(a, N); data_[i].kod_ == kod_; i++)
        if (data_[i].t_ == a) return &(data_[i]);
    return 0;
}

template<int N>
HashTable<N>::HashTable(): kod_(1), v_(0) // обнуление памяти
{
    ZeroMemory(data_, sizeof(data_));
}

typedef HashTable <5003> HashTable1;

int main()
{
    while( true ) {
        char command = 0;
        string value;
        cin >> command >> value;
        if( cin.fail() )
        {
            break;
        }
        switch( command )
        {
        case '?':
            cout << ( HashTable.Find( value ) ? "OK" : "NO" ) << endl;
            break;
        case '+':
            cout << ( HashTable.Add( value ) ? "OK" : "NO" ) << endl;
            break;
        case '-':
            cout << ( HashTable.Del( value ) ? "OK" : "NO" ) << endl;
            break;
        }
    }
    return 0;
}
