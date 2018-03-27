#include<stdio.h>
#include<stdlib.h>
struct node{
	int key;
	struct node *left,*right;
};
struct node *newnode(int item){
	struct node *temp = (struct node*)malloc(sizeof(struct node));
	temp->key=item;
	temp->left = temp->right = NULL;
	return temp;
}
void inorder(struct node *root){
	if(root != NULL){
		inorder(root->left);
		printf("%d\n",root->key);
		inorder(root->right);
	}
}
struct node* insert(struct node* node,int key){
	if(node==NULL)
		return newnode(key);
	if(key<=node->key)
		node->left=insert(node->left,key);
	else
		node->right=insert(node->right,key);
	return node;
}
int main(){
	int t,a;
	scanf("%d",&t);
	struct node *root = NULL;
	scanf("%d",&a);
	root = insert(root,a);
	t--;
	while(t--){
		scanf("%d",&a);
		insert(root,a);
	}
	inorder(root);
	return 0;
}