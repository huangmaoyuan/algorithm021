type Trie struct {
	isEnd bool
	next  [26]*Trie		//26长度的数组来指向下一层的a-z
}

/** Initialize your data structure here. */
func Constructor() Trie {
	return Trie{} 	//初始化 根节点为空
}

/** Inserts a word into the trie. */
func (this *Trie) Insert(word string) {
	//  ascii码相减
	for _, v := range word {
		if this.next[v-'a'] == nil {
			this.next[v-'a'] = &Trie{}
		}
		this = this.next[v-'a']
	}
	this.isEnd = true
}

/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
	for _, v := range word {
		if this.next[ v-'a'] == nil {
			return false
		} else {
			this = this.next[v-'a']
		}
	}
	return this.isEnd == true
}

/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
	for _, v := range prefix {
		if this.next[ v-'a'] == nil {
			return false
		} else {
			this = this.next[v-'a']
		}
	}
	return true
}



/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
