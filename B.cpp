#include <iostream>
using namespace std;
#define rep(i,n) for(int i=0;i<(n);i++)
enum COLOR {
    red = 0,
    black = 1,
};
class BTN {
public:
    int weight;
    BTN* left;
    BTN* right;
    COLOR color;
    BTN() {
        this->left = this->right = NULL;
        this->color = red;
        this->weight = 0;
    }
    BTN(BTN* left, BTN* right, COLOR color, int weight) {
        this->left = left;
        this->right = right;
        this->color = color;
        this->weight = weight;
    }
    ~BTN() {}
};
static BTN* NULLNode = NULL;
BTN* Initialize() {
    BTN* T;
    if (NULLNode == NULL) {
        NULLNode = new BTN();
        NULLNode->left = NULLNode->right = NULLNode;
        NULLNode->color = black;
        NULLNode->weight = 1e9;
    }

    T = new BTN();
    T->weight = 0 - 1e9;
    T->color = black;
    T->left = T->right = NULLNode;
    return T;
}
void Out(int weight) {
    cout << weight << endl;
}
static void Printer(BTN* T) {
    if (T != NULLNode) {
        Printer(T->left);
        Out(T->weight);
        Printer(T->right);
    }
}
void PrintTree(BTN* T) {
    Printer(T->right);
}
static BTN* MEmptyRec(BTN* T) {
    if (T != NULLNode) {
        MEmptyRec(T->right);
        MEmptyRec(T->left);
        delete T;
    }
    return NULLNode;
}
BTN* MEmpty(BTN* T) {
    T->right = MEmptyRec(T->right);
    return T;
}
BTN* Find(int x, BTN* T) {
    if (T == NULLNode) {
        return NULLNode;
    }
    if (x < T->weight) {
        return Find(x, T->left);
    }
    else if (x > T->weight) {
        return Find(x, T->right);
    }
    return T;
}
BTN* FindMin(BTN* T) {
    T = T->right;
    while (T->left != NULLNode) {
        T = T->left;
    }
    return T;
}
BTN* FindMax(BTN* T) {
    while (T->right != NULLNode) {
        T = T->right;
    }
    return T;
}
static BTN* SingleLrote(BTN* P2) {
    BTN* P1;
    P1 = P2->left;
    P2->left = P1->right;
    P1->right = P2;
    return P1;
}
static BTN* SingleRrote(BTN* P1) {
    BTN* P2;
    P2 = P1->right;
    P1->right = P2->left;
    P2->left = P1;
    return P2;
}
static BTN* Rote(int item, BTN* Parent) {
    if (item < Parent->weight) {
        return Parent->left = (item < Parent->left->weight) ?
            SingleLrote(Parent->left) :
            SingleRrote(Parent->left);
    }
    else {
        return Parent->right = (item < Parent->right->weight) ?
            SingleLrote(Parent->right) :
            SingleRrote(Parent->right);
    }
}

static BTN* X, * P, * GP, * GGP;

//再構成？
static void HandleReorient(int item, BTN* T) {
    X->color = red;
    X->left->color = black;
    X->right->color = black;
    //Xの親が赤なら叔父も赤
    if (P->color == red) {
        GP->color = red;
        //itemがお爺の要素より小さい∧親の要素よりも小さい
        //itemがお爺の要素より大きい∧親の要素よりも大きい
        if ((item < GP->weight) != (item < P->weight)) {
            P = Rote(item, GP);
        }
        X = Rote(item, GGP);
        X->color = black;
    }
    T->right->color = black;
}

BTN* del(BTN* node) {
    BTN* T, * T_P;
    int rl = 0;
    if (node->right == NULLNode) {
        if (node->left == NULLNode) {
            return NULLNode;
        }
        else {
            return node->left;
        }
    }
    if (node->left == NULLNode) {
        return node->right;
    }
    T = T_P = node->right;
    while (T->left != NULLNode) {
        T_P = T;
        T = T->left;
    }
    T->right = node->right;
    T->left = node->left;
    if (rl == 0) {
        T_P->left = NULLNode;
    }
    else if (rl == 1) {
        T_P->right = NULLNode;
    }
    return T;
}
void delN(int item, BTN* T) {
    P = X = T;
    BTN* w;
    int rl = 0, br = -1;
    while (item != X->weight) {
        if (item > X->weight) {
            P = X;
            X = X->right;
            rl = 0;
        }
        else if (item < X->weight) {
            P = X;
            X = X->left;
            rl = 1;
        }
        else {
            break;
        }
    }
    int flag = false;
    br = X->color;
    if (X->weight == 31) {
        flag = true;
    }
    if (rl == 0) {
        P->right = del(X);
        X = P->right;
    }
    else {
        P->left = del(X);
        X = P->left;
    }
    //ここから再構成
    while (X != T && X!= T->right && br == black) {
        // if (X == NULLNode)break;
        if (X == P->left) {
            w = P->right;
            if (w->color == red) {
                w->color = black;
                P->color = red;
                P = SingleLrote(P);
                w = P->right;
            }
            else if (w->right->color == black) {
                if (w->left->color == black) {
                    w->color = red;
                    X = P;
                }
                else {
                    w->left->color = black;
                    w->color = red;
                    w = SingleRrote(w);
                    w = P->right;
                    w->color = P->color;
                    P->color = black;
                    w->right->color = black;
                    P = SingleLrote(P);
                    X = T;
                }
            }
        }
        else {
            w = P->left;
            if (w->color == red) {
                w->color = black;
                P->color = red;
                P = SingleRrote(P);
                w = P->left;
            }
            else if (w->right->color == black) {
                if (w->left->color == black) {
                    w->color = red;
                    X = P;
                }
                else {
                    w->right->color = black;
                    w->color = red;
                    w = SingleLrote(w);
                    w = P->left;
                    w->color = P->color;
                    P->color = black;
                    w->left->color = black;
                    P = SingleRrote(P);
                    X = T;
                }
            }
        }
        item = X->weight;
        P = X = T;
        while (item != X->weight) {
            if (item > X->weight) {
                P = X;
                X = X->right;
                rl = 0;
            }
            else if (item < X->weight) {
                P = X;
                X = X->left;
                rl = 1;
            }
            else {
                break;
            }
        }
        br = X->color;
    }
}
BTN* Insert(int item, BTN* T) {
    X = P = GP = T;
    NULLNode->weight = item;
    while (X->weight != item) {
        GGP = GP;
        GP = P;
        P = X;
        // cout << item << X << endl;
        if (item < X->weight) {
            X = X->left;
        }
        else {
            X = X->right;
        }
        // X->left->color does not exist...&x->left doesn't exist;
        if (X->left->color == red && X->right->color == red) {
            HandleReorient(item, T);
        }
    }
    //NULLNodeに辿り着けずにwhile文が終了した＝その要素は木に既に存在している
    if (X != NULLNode) {
        return NULLNode;
    }
    X = new BTN();
    X->weight = item;
    X->left = X->right = NULLNode;

    if (item < P->weight) {
        P->left = X;
    }
    else {
        P->right = X;
    }
    HandleReorient(item, T);
    return T;
}
int main() {
    int item;
    BTN* ROOT;
    ROOT = Initialize();
    cout << "-----Insert-----" << endl;
    while (true) {
        cin >> item;
        if (item <= 0)break;
        Insert(item, ROOT);
        cout << "----Insert " << item << "----" << endl;
        PrintTree(ROOT);
    }
    cout << "-----delete-----" << endl;
    while (true) {
        cin >> item;
        if (item <= 0) {
            break;
        }
        delN(item, ROOT);
        cout << "----delete " << item << "----" << endl;
        PrintTree(ROOT);
    }
    ROOT = MEmpty(ROOT);
    return 0;
}