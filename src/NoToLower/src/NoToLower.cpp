#include "NoToLower.hpp"

using namespace h3;

NoToLowerPlugin NoToLower;


void NoToLowerPlugin::Start()
{
	BytePatch(0x61788F + 2, 0x00);
}
