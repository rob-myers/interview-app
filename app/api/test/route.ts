export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);

  return new Response(JSON.stringify({
    kvs: Array.from(searchParams.entries()),
  }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
}

export async function POST(request: Request) {
  const body = await request.json();
  const clientId = body.clientId as number;

  return new Response(JSON.stringify({
    didSomethingWithClientId: clientId,
  }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
}
