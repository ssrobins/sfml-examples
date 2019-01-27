#include <SFML/Graphics.hpp>
#include <time.h>
using namespace sf;

struct point
{float x,y;};

int main()
{
    srand(static_cast<unsigned int>(time(0)));

    RenderWindow app(VideoMode(400, 533), "Doodle Game!");
    app.setFramerateLimit(60);

    Texture t1,t2,t3;
    t1.loadFromFile("assets/background.png");
    t2.loadFromFile("assets/platform.png");
    t3.loadFromFile("assets/doodle.png");

    Sprite sBackground(t1), sPlat(t2), sPers(t3);

    point plat[20];

    for (int i=0;i<10;i++)
    {
        plat[i].x=static_cast<float>(rand()%400);
        plat[i].y=static_cast<float>(rand()%533);
    }

    float x=100,y=100,h=200;
    float dy=0;

    while (app.isOpen())
    {
        Event e;
        while (app.pollEvent(e))
        {
            if (e.type == Event::Closed)
                app.close();
        }

        if (Keyboard::isKeyPressed(Keyboard::Right)) x+=3;
        if (Keyboard::isKeyPressed(Keyboard::Left)) x-=3;

        dy+=0.2f;
        y+=dy;
        if (y>500)  dy=-10;

        if (y<h)
        for (int i=0;i<10;i++)
        {
            y=h;
            plat[i].y=plat[i].y-dy;
            if (plat[i].y>533) {plat[i].y=0; plat[i].x=static_cast<float>(rand()%400);}
        }

        for (int i=0;i<10;i++)
        {
            if ((x+50>plat[i].x) && (x+20<plat[i].x+68)
            && (y+70>plat[i].y) && (y+70<plat[i].y+14) && (dy>0))  dy=-10;
        }

        sPers.setPosition(x,y);

        app.draw(sBackground);
        app.draw(sPers);
        for (int i=0;i<10;i++)
        {
            sPlat.setPosition(static_cast<float>(plat[i].x), static_cast<float>(plat[i].y));
            app.draw(sPlat);
        }

        app.display();
    }

    return 0;
}
