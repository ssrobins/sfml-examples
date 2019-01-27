#include <SFML/Graphics.hpp>

const int numTilesHeight = 20;
const int numTilesWidth = 10;

int field[numTilesHeight][numTilesWidth] = {{ 0 }};

// Number of tiles in each tetris piece
const int numTiles = 4;

struct Point
{
    int x;
    int y;
} a[numTiles], b[numTiles];

// Number of tetris pieces
const int numPieces = 7;

// Spatial map of values in figures
// 0  1
// 2  3
// 4  5
// 6  7
int figures[numPieces][numTiles] =
{
    {1, 3, 5, 7}, // I
    {2, 4, 5, 7}, // Z
    {3, 5, 4, 6}, // S
    {3, 5, 4, 7}, // T
    {2, 3, 5, 7}, // L
    {3, 5, 7, 6}, // J
    {2, 3, 4, 5}, // O
};


class Game
{
public:
    static Game& getInstance()
    {
        static Game instance;
        return instance;
    }

    Game(Game const&) = delete;
    void operator=(Game const&) = delete;

    void checkLines()
    {
        int k = numTilesHeight - 1;
        for (auto i = numTilesHeight - 1; i > 0; i--)
        {
            int count = 0;
            for (auto j = 0; j < numTilesWidth; j++)
            {
                if (field[i][j]) count++;
                field[k][j] = field[i][j];
            }

            if (count < numTilesWidth) k--;
        }
    }

    void draw()
    {
        window.clear(sf::Color::White);
        window.draw(background);

        // Offset the pieces to match the game board
        float offsetXPixels = 28;
        float offsetYPixels = 31;

        const int tileSize = 18;

        for (auto i = 0; i < numTilesHeight; i++)
        {
            for (auto j = 0; j < numTilesWidth; j++)
            {
                if (field[i][j] == 0) continue;
                s.setTextureRect(sf::IntRect(field[i][j] * tileSize, 0, tileSize, tileSize));
                s.setPosition(static_cast<float>(j * tileSize), static_cast<float>(i * tileSize));
                s.move(offsetXPixels, offsetYPixels);
                window.draw(s);
            }
        }

        // Expand the coordinates based on tile size so the tiles don't overlap
        for (auto i = 0; i < numTiles; i++)
        {
            s.setTextureRect(sf::IntRect(colorNum * tileSize, 0, tileSize, tileSize));
            s.setPosition(static_cast<float>(a[i].x * tileSize), static_cast<float>(a[i].y * tileSize));
            s.move(offsetXPixels, offsetYPixels);
            window.draw(s);
        }

        window.draw(frame);
        window.display();
    }

    void handleEvents()
    {
        sf::Event e;
        while (window.pollEvent(e))
        {
            if (e.type == sf::Event::Closed)
                window.close();

            if (e.type == sf::Event::KeyPressed)
            {
                if (e.key.code == sf::Keyboard::Up) rotate();
                else if (e.key.code == sf::Keyboard::Down) delay = shortDelay;
                else if (e.key.code == sf::Keyboard::Left) move(-1);
                else if (e.key.code == sf::Keyboard::Right) move(1);
            }
        }
    }

    void resetValues()
    {
        dx = 0;
        delay = defaultDelay;
    }

    void tick()
    {
        if (timer > delay)
        {
            for (auto i = 0; i < numTiles; i++)
            {
                b[i] = a[i];
                a[i].y += 1;
            }

            if (collision())
            {
                for (auto i = 0; i < numTiles; i++)
                {
                    field[b[i].y][b[i].x] = colorNum;
                }
                colorNum = 1 + rand() % numPieces;
                int n = rand() % numPieces;

                // Define tile positions from 0
                // x is column number
                // y is the row number
                for (auto i = 0; i < numTiles; i++)
                {
                    // even numbers x = 0
                    // odd numbers  x = 1
                    a[i].x = figures[n][i] % 2;

                    // 0/2 = 0   1/2 = 0
                    // 2/2 = 1   3/2 = 1
                    // 4/2 = 2   5/2 = 2
                    // 6/2 = 3   7/2 = 3
                    a[i].y = figures[n][i] / 2;
                }
            }

            timer = 0;
        }
    }

    void updateTimer()
    {
        float time = clock.getElapsedTime().asSeconds();
        clock.restart();
        timer += time;
    }

    bool windowIsOpen()
    {
        return window.isOpen();
    }
private:
    Game()
        : window(sf::VideoMode(320, 480), "The Game!")
    {
        srand(static_cast<unsigned int>(time(0)));

        t1.loadFromFile("assets/tiles.png");
        t2.loadFromFile("assets/background.png");
        t3.loadFromFile("assets/frame.png");

        s.setTexture(t1);
        background.setTexture(t2);
        frame.setTexture(t3);

        dx = 0;
        colorNum = 1;
        timer = 0;

        defaultDelay = 0.3f;
        shortDelay = 0.05f;
        delay = defaultDelay;
    }

    bool collision()
    {
        for (auto i = 0; i < numTiles; i++)
        {
            if (a[i].x < 0 || a[i].x >= numTilesWidth || a[i].y >= numTilesHeight) return true;
            else if (field[a[i].y][a[i].x]) return true;
        }

        return false;
    }

    void move(int dx)
    {
        for (auto i = 0; i < numTiles; i++)
        {
            b[i] = a[i];
            a[i].x += dx;
        }
        if (collision())
        {
            for (auto i = 0; i < numTiles; i++)
                a[i] = b[i];
        }
    }

    void rotate()
    {
        Point p = a[1]; // center of rotation
        for (auto i = 0; i < numTiles; i++)
        {
            int x = a[i].y - p.y;
            int y = a[i].x - p.x;
            a[i].x = p.x - x;
            a[i].y = p.y + y;
        }
        if (collision())
        {
            for (auto i = 0; i < numTiles; i++)
                a[i] = b[i];
        }
    }

    sf::RenderWindow window;
    sf::Texture t1, t2, t3;
    sf::Sprite s, background, frame;
    sf::Clock clock;

    int dx;
    int colorNum;
    float timer;

    float defaultDelay;
    float shortDelay;
    float delay;
};


int main()
{
    auto& game = Game::getInstance();

    while (game.windowIsOpen())
    {
        game.updateTimer();

        game.handleEvents();

        game.tick();

        game.checkLines();

        game.resetValues();

        game.draw();
    }

    return 0;
}
