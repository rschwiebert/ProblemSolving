#include <cstddef>
#include <algorithm>
#include <iostream>

/**
 * Definition for binary tree
*/
struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int minDepth(TreeNode *root) {
        if (root == NULL){
            return 0;
        } else if (root->left == NULL && root->right == NULL){
            return 1;
        } else if (root->left == NULL && root->right != NULL){
            return 1 + minDepth(root->right);
        } else if (root->left != NULL && root->right == NULL){
            return 1 + minDepth(root->left);
        } else if (root->left != NULL && root->right != NULL){
            return 1 + std::min(minDepth(root->left), minDepth(root->right));
        }
    }
};

int main(){
	Solution sol;
	struct TreeNode node1(1);
	struct TreeNode node2(2,NULL,node1);
	std::cout << sol.minDepth(&node2);
}


