import sys
import ffmpeg


if __name__ == '__main__':
    print(sys.argv)
    print(len(sys.argv))
    print(sys.argv[len(sys.argv) - 1])
    with open("list.txt", "w") as list:
        for i in range(1, len(sys.argv) - 1):
            list.write(f"file {sys.argv[i]}\n")
    ffmpeg.input("list.txt", format='concat', safe=0).output(sys.argv[len(sys.argv) - 1], c='copy').run()
