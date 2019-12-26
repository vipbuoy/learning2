def comma(value):
    st=''
    for i in value:
        if i!=value[len(value)-1]:
            st=st+i+', '

    st=st+'and '+value[len(value)-1]
    return st


spam=['apples','bananas','tofu','cats']
st=comma(spam)
print(st)
