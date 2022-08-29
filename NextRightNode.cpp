#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    struct Node *left;
    struct Node *right;
    struct Node *next;

    Node(int x)
    {
        data = x;
        left = NULL;
        right = NULL;
    }
};

class Solution
{
public:
    Node *nextRight(Node *root, int key)
    {
        //code here
        if (root == NULL)
            return 0;
            
        int current = 0;
        
        queue<Node *> addresses;
        queue<int> levels;
        
        addresses.push(root);
        levels.push(current);
        
        while (addresses.size())
        {
            Node *temp = addresses.front();
            current = levels.front();
            addresses.pop();
            levels.pop();
            
            if (temp->data == key)
            {
                if ((addresses.size() == 0) || (levels.front() != current))
                {
                    Node *ans = new Node(-1);
                    return ans;
                }
                    
                return addresses.front();
            }
            
            if (temp->left != NULL)
            {
                addresses.push(temp->left);
                levels.push(current + 1);
            }
            if (temp->right != NULL)
            {
                addresses.push(temp->right);
                levels.push(current + 1);
            }
        }
        Node *ans = new Node(-1);
        return ans;
    }
};