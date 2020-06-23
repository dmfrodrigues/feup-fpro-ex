import statistics as st
def batch_norm(alist, batch_size):
    for l in range(0,len(alist),batch_size):
        m = st.median(alist[l:min(l+batch_size, len(alist))])
        yield list(map(lambda x: x - m, alist[l:min(l+batch_size, len(alist))]))