#include <memory>

#include "bst_node.h"
#include "test_framework/generic_test.h"
using std::unique_ptr;

// class FindFirst {

//   public:
//   FindFirst(const unique_ptr<BstNode<int>>& tree,
//                                     int k){

//                                     }
// }
class FindFirst
{

public:
  BstNode<int> *bstN = nullptr;
  int minGtVal = std::numeric_limits<int>::max();

  void FindFirstGreaterThanK(const unique_ptr<BstNode<int>> &tree,
                             int k)
  {
    // TODO - you fill in here.
    if (tree == nullptr)
    {
      return;
    }

    if (tree->data > k)
    {
      if (tree->data < minGtVal)
      {
        minGtVal = tree->data;
        bstN = tree.get();
      }
      FindFirstGreaterThanK(tree->left, k);
    }
    else
    {
      FindFirstGreaterThanK(tree->right, k);
    }
  }
};

BstNode<int> *FindFirstGreaterThanK(const unique_ptr<BstNode<int>> &tree, int k)
{
  BstNode<int> *subtree = tree.get();
  BstNode<int> *first_so_far = nullptr;
  while (subtree)
  {
    if (subtree->data > k)
    {
      first_so_far = subtree; // if 
      subtree = subtree->left.get();
    }
    else
    {
      subtree = subtree->right.get();
    }
  }
  return first_so_far;
}
int FindFirstGreaterThanKWrapper(const unique_ptr<BstNode<int>> &tree, int k)
{
  auto result = FindFirstGreaterThanK(tree, k);
  return result ? result->data : -1;
}

int main(int argc, char *argv[])
{
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"tree", "k"};
  return GenericTestMain(args, "search_first_greater_value_in_bst.cc",
                         "search_first_greater_value_in_bst.tsv",
                         &FindFirstGreaterThanKWrapper, DefaultComparator{},
                         param_names);
}
