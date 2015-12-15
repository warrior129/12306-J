from Ticket import train
import getopt,sys,time

def main(argv):

    d = time.strftime("%Y-%m-%d",time.localtime())
    f = '济南'
    t = '兖州'

    try:
        options,args = getopt.getopt(sys.argv[1:],"hd:f:t:")
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(1)

    for name,value in options:
        if name in ("-d"):
            d= value
        elif name in ("-f"):
            f=value
        elif name in ("-t"):
            t=value

    tr = train(d,f,t)
    tr.query_ticket()

if __name__ == '__main__' :
    main(sys.argv)